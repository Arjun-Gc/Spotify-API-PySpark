from step05stage_table import db_manager
import csv,os

def track_into_csv(csv_file_path,table_name): 
    csv_files = [f for f in os.listdir(csv_file_path) if f.endswith(".csv")]
    csv_file_name = csv_files[0]
    # print(csv_file_name)
    with open(f"{csv_file_path}\\{csv_file_name}", 'r',encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = list(csv_reader)
        track_query = f'INSERT INTO {table_name} (playlist_name,playlist_owner_name,playlist_tracks,playlist_url) VALUES (%s, %s, %s, %s)'
        
    for row in data_list:
        playlist_name = row['playlist_name']   
        playlist_owner_name = row['playlist_owner_name']
        playlist_tracks = row['total_track']
        playlist_url = row['playlist_url']

        db_manager.cursor.execute(track_query, (playlist_name,playlist_owner_name,playlist_tracks,playlist_url))

    print("Successfully loaded")
    db_manager.conn.commit()
    db_manager.close_connection()

csv_file_path =r'C:\Users\VICTUS\Desktop\grow by data\spotify_api\clean_playlist.csv'
table_name = 'playlist_stage_table'
track_into_csv(csv_file_path, table_name)

