from googleapiclient.discovery import build

def get_youtube_music_links(api_key, song_names):
    youtube = build('youtube', 'v3', developerKey=api_key)
    links = []

    for song_name in song_names:
       
        search_response = youtube.search().list(
            q=song_name,
            part='id',
            type='video'
        ).execute()

        
        if 'items' in search_response:
            video_id = search_response['items'][0]['id']['videoId']

           
            link = f'https://music.youtube.com/watch?v={video_id}'
            links.append(link)

    return links


api_key = 'AIzaSyDYyrQ0N4bWLwsL-JVXeeY6-6ZKSmQEdxg'

song_names_list = ['apna bna le', 'duniya', 'kese hua']

links = get_youtube_music_links(api_key, song_names_list)
for song_name, link in zip(song_names_list, links):
    print(f'{song_name}: {link}')
