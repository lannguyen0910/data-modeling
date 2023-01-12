## File structure

```sql_queries.py``` -> contains sql queries for dropping and creating fact and dimension tables. Also, contains insertion query template.

```database.py``` -> contains code for setting up database. Running this file creates **sparkifydb** and also creates the fact and dimension tables.

```etl.py``` -> read and process **song_data** and **log_data**