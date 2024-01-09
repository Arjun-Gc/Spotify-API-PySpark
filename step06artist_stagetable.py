from step05stage_table import db_manager,cursor
import csv



def load_artist_from_csv(csv_file_path, table_name):
    try: 
        if not db_manager.cursor:
            db_manager.connect()
        
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = list(csv_reader)
            artist_query = f'INSERT INTO {table_name} (artist_name_artist, artist_id, artist_populartity, artist_genres, artist_followers) VALUES (%s, %s, %s, %s, %s)'
            
        for row in data_list:
            artist_name_artist = row['artist_name']
            artist_id = row['artist_id']
            artist_popularity = row['artist_popularity']
            artist_genres = row['genres']
            artist_followers = row['artist_followers']

            db_manager.cursor.execute(artist_query, (artist_name_artist, artist_id, artist_popularity, artist_genres, artist_followers))

        print("Successfully loaded")
        db_manager.conn.commit()
        db_manager.close_connection()
    except OSError as err:
            print(f"Error: {err}")
        
csv_file_path = './clean_artist.csv/artist_pyspark.csv'
table_name = 'artist_stage_table'
load_artist_from_csv(csv_file_path, table_name)