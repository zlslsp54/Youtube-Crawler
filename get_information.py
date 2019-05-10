import pytube
from youtube_transcript_api import YouTubeTranscriptApi

# 정보 다운로드
def download_info(items):
    title = items['items'][0]['snippet']['title']
    description = items['items'][0]['snippet']['description']
    publishedAt = items['items'][0]['snippet']['publishedAt']
    if items['items'][0]['snippet'].get('defaultLanguage') is None:
        defaultLanguage = "None"
    else:
        defaultLanguage = items['items'][0]['snippet']['defaultLanguage']
    return [title, description, defaultLanguage, publishedAt]

# 자막 다운로드
def download_caption(video_id):
    caption = YouTubeTranscriptApi.get_transcript(video_id)
    videos_caption = [list(x.values()) for x in caption]
    return videos_caption
