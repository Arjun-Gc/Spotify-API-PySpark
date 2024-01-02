from api_spotify02 import artists,albums,songs,playlist
import csv

file_path = "artists.csv"
artist_data = artists["artists"]["items"]
#agadi bata aayeko artists ley display garauni data bhitra ko artist ani artist tyo bhitra ko item(curly braces bhitrako)
field_names1 = ["artist_name", "id", "href", "popularity", "genres",'followers']
with open(file_path, 'w', newline = '', encoding = 'utf-8') as csv_file1:
    csv_writer = csv.DictWriter(csv_file1, fieldnames=field_names1)
    csv_writer.writeheader()
    
    for artist in artist_data:
        csv_writer.writerow({
            'artist_name': artist.get('name', ''),
            #name bhaye pathauni natra empty''
            'id': artist.get('id', ''),
            'href': artist.get('href', ''),
            'popularity': artist.get('popularity', ''),
            'genres': ', '.join(artist.get('genres', [])) if artist.get('genres') else 'other' ,
            'followers': artist.get("followers", [{}]).get("total", "")
            #yo bhanya genres dherai bhaye comma ley separate garera dekhauni natra khali bhaye '' khali chadni
            
        })
    print("search_for_artist data is written to csv")
    

album_file='album.csv'
album_field=['album_id','album_name','artist_name','url','release_date']
albums=albums['albums']['items']
with open(album_file, 'w', newline= '', encoding='utf-8') as album_csv:
    csv_writer=csv.DictWriter(album_csv, fieldnames =album_field)
    csv_writer.writeheader()
    for album in albums:
        csv_writer.writerow({
            'album_id':album.get('id',''),
            'album_name': album.get("name", ''),
            'artist_name':album.get('artists',[{}]) [0].get('name',''),
            'url':album.get('external_url',{}).get('href',''),
            "release_date": album.get("release_date", ''),
        })
        
        
file_path4 = "tracks.csv"
field_names4 = ['track_name', 'artist_names', 'album_name',  'release_date', 'total_tracks', 'popularity', 'track_url']
track_data = songs['tracks']['items']
with open(file_path4, 'w', newline = '', encoding="utf-8") as csv_file4:
    csv_writer = csv.DictWriter(csv_file4, fieldnames=field_names4)
    csv_writer.writeheader()
    
    for track in track_data:
        csv_writer.writerow({
            "track_name": track.get('name', ''),
            "artist_names": [artist['name'] for artist in track['artists']],
            "album_name": track.get('album', {}).get('name', ''),
            "release_date": track.get('album', {}).get('release_date', ''),
            "total_tracks": track.get('album', {}).get('total_tracks', 0),
            "track_url": track.get('external_urls', {}).get('spotify', '')

        })
    print("search_for_tracks is written to csv")
    
    
file_path3 = "Playlist.csv"
field_names3 = ["playlist_name", "owner_name", "total_track", "playlist_url"]
playlists_data = playlist["playlists"]["items"]
with open(file_path3, 'w', newline = '', encoding="utf-8") as csv_file3:
    csv_writer = csv.DictWriter(csv_file3, fieldnames=field_names3)
    csv_writer.writeheader()
    
    for playlist in playlists_data:
        csv_writer.writerow({
            "playlist_name": playlist.get("name",''),
            "owner_name": playlist.get("owner", {}).get("display_name",''),
            "total_track": playlist.get("tracks", {}).get("total", 0),
            #total nabhaye 0
            "playlist_url": playlist.get("external_urls", {}).get("spotify",'')
        })
    print("search_for_playlists is written to csv")
    
