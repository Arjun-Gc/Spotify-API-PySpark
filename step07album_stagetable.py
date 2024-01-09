from step05stage_table import db_manager
import csv,os


def album_into_csv(csv_file_path,table_name): 
    csv_files = [f for f in os.listdir(csv_file_path) if f.endswith(".csv")]
    csv_file_name = csv_files[0]
    # print(csv_file_name)
    with open(f"{csv_file_path}\\{csv_file_name}", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = list(csv_reader)
        album_query = f'INSERT INTO {table_name} (album_name,album_id,album_singers,album_url,album_release_year) VALUES (%s, %s, %s, %s, %s)'
        
    for row in data_list:
        album_name = row['album_name']
        album_id = row['album_id']
        album_singers = row['artist_name']
        album_url = row['url']
        album_release_year = row['release_year']

        db_manager.cursor.execute(album_query, (album_name, album_id, album_singers, album_url, album_release_year))

    print("Successfully loaded")
    db_manager.conn.commit()
    db_manager.close_connection()

csv_file_path =r'C:\Users\VICTUS\Desktop\grow by data\spotify_api\clean_album.csv'
table_name = 'album_stage_table'
album_into_csv(csv_file_path, table_name)

