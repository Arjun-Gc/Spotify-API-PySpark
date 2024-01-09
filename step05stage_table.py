import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv('database')


class MySQLDatabaseManager:
    def __init__(self, host, user, password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database= database
        self.connection = None
        self.cursor = None
   

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
             
            self.cursor= self.conn.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        
    def create_database(self, database_name):
        try: 
            # Ensure the connection and cursor are initialized
            if not self.conn or not self.cursor:
                self.connect()

            self.cursor.execute(f"CREATE DATABASE IF NOT EXIST {database_name}")
            print(f"Database '{database_name}' created successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            
    def create_stage_table(self,artist_query):
        try:
        # Ensure the connection and cursor are initialized
            if not self.conn or not self.cursor:
                self.connect()

            # Execute the query
            self.cursor.execute(artist_query)
            print("Table created successfully.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")     
    
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")


if __name__ == "__main__":
 
    mysql_host = host
    mysql_user = user
    mysql_password = password
    new_database_name = database

    # Create an instance of the MySQLDatabaseManager
    db_manager = MySQLDatabaseManager(host, user, password,database)

    # Connect to MySQL
    if db_manager.connect():
        print('Sucessfully connected to the database')
    # Create a new MySQL database
    db_manager.create_database(new_database_name)
    
    artist='''CREATE TABLE IF NOT EXISTS artist_stage_table (
    artist_name_artist VARCHAR(255),
    artist_id VARCHAR(255) Primary key,
    artist_populartity INT,
    artist_genres VARCHAR(255),
    artist_followers  INT
    );   '''

    
    album='''CREATE TABLE IF NOT EXISTS album_stage_table (
    album_name VARCHAR(255),
    album_id VARCHAR(255) Primary Key,
    album_singers VARCHAR(255),
    album_url VARCHAR(255),
    album_release_year INT
    ); '''
    
    playlist='''CREATE TABLE IF NOT EXISTS playlist_stage_table (
    playlist_name VARCHAR(255),
    playlist_owner_name VARCHAR(255) ,
    playlist_tracks INT,
    playlist_url VARCHAR(255)
    ); '''
    
    track='''CREATE TABLE IF NOT EXISTS track_stage_table (
    track_name_ VARCHAR(255),
    track_artist_name VARCHAR(255),
    track_album_name VARCHAR(255),
    track_track_no int ,
    track_url VARCHAR(255),
    track_release_year INT,
    track_popularity int
    ); '''
    db_manager.create_stage_table(artist)
    db_manager.create_stage_table(album)
    db_manager.create_stage_table(track)
    db_manager.create_stage_table(playlist)

    # Close the connection
    db_manager.close_connection()


db_manager = MySQLDatabaseManager(host, user, password, database)
cursor=db_manager.connect()
