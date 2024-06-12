from youtube_transcript_api import YouTubeTranscriptApi as yta
import os

def getTranscript(vidId, name):
    data = yta.get_transcript(vidId)
    transcript = ''
    for value in data:
        for key, val in value.items():
            if key == 'text':
                transcript += val + ' '
    l = transcript.splitlines()
    final_tra = " ".join(l)

    album_dir = os.path.join("albums", name)
    with open(os.path.join(album_dir, "Fantano.txt"), "w", encoding="utf-8") as file:
        file.write(final_tra)
