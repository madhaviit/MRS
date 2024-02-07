import pandas as pd
import pickle
data = pd.read_csv("D:/New folder/data3.csv")

def recommend_songs(input_songs, data, cluster_model, song_cluster_model, pca_model):
    input_clusters = []
    for song in input_songs:
        genre_value = data[data['track_name'] == song['track_name']]['Genre'].values
        for i in range(len(genre_value)):
            cluster = data[data['Genre'] == genre_value[i]]['cluster_label'].values
            if len(cluster) > 0:
                input_clusters.extend(cluster)

    if not input_clusters:
        return "No recommendation available, input songs not found in the dataset."

    recommended_cluster = max(set(input_clusters), key=input_clusters.count)
    recommended_songs = data[data['cluster_label'] == recommended_cluster]

    if recommended_songs.empty:
        return "No recommendation available for the given input songs and cluster."

    recommended_songs_sample = recommended_songs.sample(40)
    return recommended_songs_sample


with open('genre_cluster_model.pkl', 'rb') as model_file:
    genre_cluster_model = pickle.load(model_file)

with open('song_cluster_model.pkl', 'rb') as model_file:
    song_cluster_model = pickle.load(model_file)

with open('pca_model.pkl', 'rb') as model_file:
    pca_model = pickle.load(model_file)
    # Assume you have a predefined list of input songs
predefined_input_songs = [
    {'track_name': 'Lose Control (feat. Ciara & Fat Man Scoop)'},
    {'track_name': 'Toxic'},
    {'track_name': 'Rock Your Body'},
    {'track_name': 'My Boo'},
    {'track_name': 'Yeah!'} ,
]

lst=[]
recommended_tracks = recommend_songs(predefined_input_songs, data, genre_cluster_model, song_cluster_model, pca_model)
for index, row in recommended_tracks.iterrows():
  lst.append(row['unique_id'])

