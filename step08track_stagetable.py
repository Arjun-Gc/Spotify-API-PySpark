from step05stage_table import db_manager
import csv,os



def track_into_csv(csv_file_path,table_name): 
    csv_files = [f for f in os.listdir(csv_file_path) if f.endswith(".csv")]
    csv_file_name = csv_files[0]
    # print(csv_file_name)
    with open(f"{csv_file_path}\\{csv_file_name}", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = list(csv_reader)
        track_query = f'INSERT INTO {table_name} (track_name_,track_artist_name,track_album_name,track_track_no, track_url, track_release_year, track_popularity  ) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        
    for row in data_list:
        track_name_ = row['track_name']   
        track_artist_names = row['artist_names']
        track_album_name = row['album_name']
        track_release_year = row['track_release_year']
        total_tracks_no = row['total_tracks']
        track_popularity= row['track_popularity']
        track_url = row['track_url']
        

        db_manager.cursor.execute(track_query, (track_name_,track_artist_names,track_album_name,total_tracks_no,track_url,track_release_year,track_popularity))

    print("Successfully loaded")
    db_manager.conn.commit()
    db_manager.close_connection()

csv_file_path =r'C:\Users\VICTUS\Desktop\grow by data\spotify_api\clean_track.csv'
table_name = 'track_stage_table'
track_into_csv(csv_file_path, table_name)

