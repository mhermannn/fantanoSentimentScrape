import os
from scraping.pullCommentsDF import comments_to_DF 
from scraping.pullCommentsTXT import comments_to_TXT
from scraping.getFantanoTranscript import getTranscript
from sentiment.barGraphs import barGraphs
from sentiment.emotionBars import emotionBars

def organizer(vidId, name):
    album_dir = os.path.join("albums", name)
    if not os.path.exists(album_dir):
        os.makedirs(album_dir)
    
    DataFrame = comments_to_DF(vidId)
    comments_to_TXT(vidId, name)
    getTranscript(vidId, name)
    
    df_path = os.path.join(album_dir, "comments.csv")
    DataFrame.to_csv(df_path, index=False)

    barGraphs(name)
    emotionBars(name)