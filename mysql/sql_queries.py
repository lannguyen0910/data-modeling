# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
	songplay_id INT AUTO_INCREMENT PRIMARY KEY,
	start_time TIMESTAMP,
	user_id INT,
	level VARCHAR(255) NOT NULL,
	song_id VARCHAR(255),
	artist_id VARCHAR(255),
	session_id INT NOT NULL,
	location VARCHAR(255),
	user_agent TEXT,
	FOREIGN KEY (start_time) REFERENCES time(start_time),
	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (song_id) REFERENCES songs(song_id),
	FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
)""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
	user_id INT PRIMARY KEY,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	gender CHAR(1),
	level VARCHAR(255) NOT NULL UNIQUE
)""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
	song_id VARCHAR(255) PRIMARY KEY,
	title VARCHAR(255),
	artist_id VARCHAR(255),
	year INT CHECK (year >= 0),
	duration FLOAT,
	FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
)""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
	artist_id VARCHAR(255) PRIMARY KEY,
	name VARCHAR(255),
	location VARCHAR(255),
	latitude DECIMAL(9,6),
	longitude DECIMAL(9,6)
)""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
	start_time TIMESTAMP PRIMARY KEY,
	hour INT NOT NULL CHECK (hour >= 0),
	day INT NOT NULL CHECK (day >= 0),
	week INT NOT NULL CHECK (week >= 0),
	month INT NOT NULL CHECK (month >= 0),
	year INT NOT NULL CHECK (year >= 0),
	weekday VARCHAR(255) NOT NULL
)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)""")


# Updating the user level on conflict
user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                        VALUES (%s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE user_id = VALUES(user_id), level = VALUES(level)
                        """)

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                        VALUES (%s, %s, %s, %s, %s)""")


# Artist location, latitude and longitude might change and need to be updated.
artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)
                        VALUES (%s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE location = VALUES(location), latitude = VALUES(latitude), longitude = VALUES(longitude);""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""")

# FIND SONGS

song_select = ("""
    SELECT song_id, artists.artist_id
    FROM songs
    JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create,
                        song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
