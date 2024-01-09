from step05stage_table import db_manager
import os

def create_table(table_name):
    query= '''CREATE TABLE IF NOT EXISTS dim_track (
     track_name  VARCHAR(255),
     track_id  INT AUTO_INCREMENT PRIMARY KEY,
     track_album_name  VARCHAR(255),
     track_total_no INT,
     track_release_year INT
    );   '''
    db_manager.cursor.execute(query)
    db_manager.conn.commit()
    print (f'sucessuflly created {table_name}')
    

def dim_artist():
    query = '''
    INSERT INTO dim_artist (artist_id, artist_name_artist, artist_followers)
SELECT s.artist_id, s.artist_name_artist, s.artist_followers
FROM artist_stage_table s
LEFT JOIN dim_artist da ON s.artist_id = da.artist_id 
WHERE da.artist_id IS NULL
GROUP BY da.artist_id;

        '''
    db_manager.cursor.execute(query)
    db_manager.conn.commit()

def dim_album():
    query='''  INSERT INTO dim_album(album_name,album_id,album_artist,album_release_year)
    select  s.album_name,s.album_id,s.album_singers,s.album_release_year from album_stage_table s
    left join dim_album da on  s.album_id= da.album_id
    where da.album_id is null
    group by s.album_id ,s.album_name; 
    '''
    db_manager.cursor.execute(query)
    db_manager.conn.commit()

def dim_track():
    query=''' 
    INSERT INTO dim_track  (track_name,track_album_name,track_total_no,track_release_year)
    select s.track_name_, s.track_album_name,s.track_track_no,s.track_release_year  from track_stage_table s
    left join dim_track dt on s.track_name_ = dt.track_name
    where dt.track_name is null
    ;
    '''
    db_manager.cursor.execute(query)
    db_manager.conn.commit()
    
    
def dim_playlist():
    query=''' INSERT INTO dim_playlist (playlist_name, playlist_owner_name)
SELECT s.playlist_name, s.playlist_owner_name
FROM playlist_stage_table s
LEFT JOIN dim_playlist dp ON s.playlist_name = dp.playlist_name
WHERE dp.playlist_name IS NULL
;
  '''
    db_manager.cursor.execute(query)
    db_manager.conn.commit()
    

dim_playlist()



