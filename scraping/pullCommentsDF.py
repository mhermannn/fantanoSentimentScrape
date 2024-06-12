import googleapiclient.discovery
import pandas as pd
def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
def comments_to_DF(vidId):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = get_api_key('key.txt')

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=vidId,
        maxResults=20000
    )
    response = request.execute()

    comments = []

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([
            comment['authorDisplayName'],
            comment['publishedAt'],
            comment['updatedAt'],
            comment['likeCount'],
            comment['textDisplay']
        ])

    df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])
    return df

        