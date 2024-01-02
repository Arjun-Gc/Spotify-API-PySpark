from token_generate01 import token 
from requests import get
import json

def get_auth_token(token):
    return {"Authorization": "Bearer " + token}

url = "https://api.spotify.com/v1/search"
header = get_auth_token(token)


def search_for_artist(id):
    #documentation ma search by item ma gayera herni
    query = f'?q={id}&type=artist'
    #yedi artist matrai haina track ni chaiye comma ley separate like artist, track, playlist and so on
    #limit = 1 ley pailo artist that pop out dekhaucha
    query_url = url + query
    #mathi ko q agadiko ? yesma + lekhera joddda pani hunthyo
    result = get(query_url, headers = header)
    #get request garya(yaad cha ni postman wala? same)
    json_result = json.loads(result.content)
    #result ko content json string ma huncha teslai python dictionary ma lagni
    return json_result
    
    
def get_album(id):
    query= url + f"?q={id}&type=album"
    result=get(query,headers=header)
    data=json.loads(result.content)
    return (data) 


def get_artist_songs(id):
    query= url + f"?q={id}&type=track"
    result=get(query,headers=header)
    json_result=json.loads(result.content)
    return json_result
    
def get_artist_album(id):
    query= url + f"?q={id}&type=album"
    result=get(query,headers=header)
    data=json.loads(result.content)
    return(data)
    
    
    
def get_artist_playlist(id):
    query= url + f"?q={id}&type=playlist"
    result=get(query,headers=header)
    data=json.loads(result.content)
    return data

           


id = "remaster%2520track%3ADoxy%2520artist%3Amichael %2520jackson"  
artists = search_for_artist(id)
albums=get_artist_album(id)
songs=get_artist_songs(id)
playlist=get_artist_playlist(id)
print(albums)

    
    

