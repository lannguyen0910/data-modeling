import os
import glob

import pandas as pd
import mysql.connector
from loguru import logger

from configs import HOST, PASSWD, USER, DATABASE, AUTH_PLUGIN
from sql_queries import artist_table_insert, user_table_insert, song_table_insert, time_table_insert, songplay_table_insert, song_select


def process_song_file(cur, filepath):
    """
    Process songs files and insert records into the Postgres database.
    :param cur: cursor reference
    :param filepath: complete file path for the file to load
    """

    # open song file
    df = pd.DataFrame(
        [pd.read_json(filepath, typ='series', convert_dates=False)])

    for value in df.values:
        num_songs, artist_id, artist_latitude, artist_longitude, artist_location, artist_name, song_id, title, duration, year = value

        # insert artist record
        artist_data = (artist_id, artist_name, artist_location,
                       artist_latitude, artist_longitude)
        cur.execute(artist_table_insert, artist_data)

        # insert song record
        song_data = (song_id, title, artist_id, year, duration)
        cur.execute(song_table_insert, song_data)

    logger.info(f"Records inserted for file {filepath}")


def process_log_file(cur, filepath):
    """
    Process Event log files and insert records into the Postgres database.
    :param cur: cursor reference
    :param filepath: complete file path for the file to load
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == "NextSong"].astype({'ts': 'datetime64[ms]'})

    # convert timestamp column to datetime
    t = pd.Series(df['ts'], index=df.index)

    # insert time data records
    column_labels = ["start_time", "hour", "day",
                     "week", "month", "year", "weekday"]
    time_data = []
    for data in t:
        timestamp = data.strftime('%Y-%m-%d %H:%M:%S')
        time_data.append([timestamp, data.hour, data.day, data.weekofyear,
                         data.month, data.year, data.day_name()])

    time_df = pd.DataFrame.from_records(data=time_data, columns=column_labels)

    for _, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]
    user_df['userId'] = user_df['userId'].astype(int)
    user_df = user_df.rename(columns={'userId': 'user_id',
                                      'firstName': 'first_name',
                                      'lastName': 'last_name'})

    # insert user records
    for _, row in user_df.iterrows():
        cur.execute(user_table_insert, list(row))

    # insert songplay records
    for _, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        timestamp = row.ts
        timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

        # insert songplay record
        songplay_data = [timestamp, int(row.userId), row.level, songid,
                         artistid, row.sessionId, row.location, row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    Driver function to load data from songs and event log files into Postgres database.
    :param cur: a database cursor reference
    :param conn: database connection reference
    :param filepath: parent directory where the files exists
    :param func: function to call
    """
    # get all files matching extension from directory
    all_files = []
    for root, _, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    logger.info('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        logger.info('{}/{} files processed.'.format(i, num_files))


def main():
    """
    Driver function for loading songs and log data into Postgres database
    """
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
        database=DATABASE,
        auth_plugin=AUTH_PLUGIN,
        autocommit=True
    )
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song/song_data',
                 func=process_song_file)
    process_data(cur, conn, filepath='data/song/log_data',
                 func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
    logger.info("\n\nFinished processing!!!\n\n")
