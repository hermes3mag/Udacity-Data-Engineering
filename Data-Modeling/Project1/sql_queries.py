# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id int not null primary key, first_name varchar, last_name varchar, gender varchar, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar not null primary key, title varchar, artist_id varchar, year int, duration int);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar not null primary key, name varchar, location varchar, latitude float, longitude float);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time varchar not null primary key, hour int, day int, week int, month int, year int, weekday int);""")

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (\
                            songplay_id serial primary key, \
                            start_time varchar not null, \
                            user_id int not null, \
                            level varchar , \
                            song_id varchar, \
                            artist_id varchar, \
                            session_id varchar not null, \
                            location varchar, \
                            user_agent varchar)")


# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) on conflict (songplay_id) do nothing""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES(%s,%s,%s,%s,%s) on conflict (user_id) do update set first_name=excluded.first_name,last_name=excluded.last_name,gender=excluded.gender,level=excluded.level""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES(%s,%s,%s,%s,%s) on conflict (song_id) do nothing""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES(%s,%s,%s,%s,%s) on conflict (artist_id) do nothing""")

time_table_insert = ("""INSERT INTO TIME(start_time, hour, day, week, month, year, weekday) VALUES(%s,%s,%s,%s,%s,%s,%s) on conflict (start_time) do nothing""")

# FIND SONGS
#find the song ID and artist ID based on the title, artist name, and duration of a song.
song_select = ("""SELECT s.song_id, a.artist_id FROM songs s JOIN artists a ON s.artist_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]