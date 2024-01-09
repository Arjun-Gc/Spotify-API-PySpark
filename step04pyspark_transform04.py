from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format,regexp_replace

spark=SparkSession.builder.appName("album_table").getOrCreate()

df_album= spark.read.csv("album.csv",header=True)
df_artist= spark.read.csv('artists.csv',header=True)
df_playlist=spark.read.csv('playlist.csv',header=True)
df_track=spark.read.csv('tracks.csv',header=True)
# renaming headers
df_album = df_album.withColumnRenamed("release_date", "release_year")
df_artist= df_artist.drop('href')
df_artist= df_artist.withColumnRenamed('popularity','artist_popularity')
df_artist= df_artist.withColumnRenamed('id','artist_id')
df_artist= df_artist.withColumnRenamed('followers','artist_followers')
df_track = df_track.withColumnRenamed("release_date", "track_release_year")
df_track = df_track.withColumnRenamed("artist_name", "track_artist_name")
df_track= df_track.withColumnRenamed('popularity','track_popularity')
df_playlist=df_playlist.withColumnRenamed('owner_name','playlist_owner_name')


# Transform data 
df_album = df_album.withColumn("release_year", date_format(col("release_year"), "yyyy"))
df_track =df_track.withColumn('track_release_year',date_format(col('track_release_year'),'yyyy'))




df_album.write.csv('clean_album.csv',header=True,mode='overwrite')
df_track.write.csv('clean_track.csv',header=True,mode='overwrite')
df_playlist.write.csv('clean_playlist.csv',header=True,mode='overwrite')
df_artist.write.csv('clean_artist.csv',header=True,mode='overwrite')
 