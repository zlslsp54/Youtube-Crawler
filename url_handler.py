import re
import requests
import json

def get_api_information(url, apiKey):
    pat = re.compile("(v=)([a-zA-Z0-9-_]{11})")
    video_id = pat.search(url).group(2)
    part = "snippet"
    target_url = 'https://www.googleapis.com/youtube/v3/videos?part=' + part + '&id=' + video_id + '&key=' + apiKey
    response = requests.get(target_url).text
    items = json.loads(response)

    return video_id, items
