import googleapiclient.discovery
import googleapiclient.errors
import os
def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
def comments_to_TXT(vidId, name):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = get_api_key('key.txt')

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    
    album_dir = os.path.join("albums", name)
    if not os.path.exists(album_dir):
        os.makedirs(album_dir)
    
    max_retries = 5
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=vidId,
        maxResults=100
    )

    with open(os.path.join(album_dir, "comments.txt"), "w", encoding="utf-8") as file:
        while request is not None:
            try:
                response = request.execute()
                for item in response['items']:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    file.write(comment + "\n")
                
                request = youtube.commentThreads().list_next(request, response)
            except googleapiclient.errors.HttpError as e:
                if e.resp.status in [403, 500, 503]:
                    print(f"Error {e.resp.status}: {e.content}. Retrying...")
                    time.sleep(5)  # wait before retrying
                    max_retries -= 1
                    if max_retries == 0:
                        print("Max retries reached. Exiting.")
                        break
                else:
                    print(f"An error occurred: {e}")
                    break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break
