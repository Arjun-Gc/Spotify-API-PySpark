from step05stage_table import db_manager

def fact_tabel():
    query='''
    CREATE TABLE IF NOT EXISTS fact_table (
    artist_id VARCHAR(255),
    album_id VARCHAR(255),
    track_id INT,
    playlist_id INT,
    release_year INT,
    FOREIGN KEY (artist_id) REFERENCES dim_artist(artist_id),
    FOREIGN KEY (album_id) REFERENCES dim_album(album_id),
    FOREIGN KEY (track_id) REFERENCES dim_track(track_id),
    FOREIGN KEY (playlist_id) REFERENCES dim_playlist(playlist_id)
);'''
    db_manager.cursor.execute(query)
    db_manager.conn.commit()
    

def insert_into_fact_tabel():
    query=''' INSERT INTO fact_table (artist_id, album_id, release_year)
SELECT da.artist_id, dal.album_id, dal.album_release_year
FROM dim_artist da
JOIN artist_stage_table sa ON da.artist_id = sa.artist_id
JOIN album_stage_table sal ON dal.album_id = sal.album_id
GROUP BY da.artist_id, dal.album_id;

    
    '''
    db_manager.cursor.execute(query)
    db_manager.conn.commit()
    
insert_into_fact_tabel()