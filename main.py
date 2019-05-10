from url_handler import get_api_information
from get_information import download_info, download_caption
from database_handler_mysql import insert_info, insert_caption, close_connection

#from database_handler import close_connection

url = input("URL address: ")
apiKey = input("API key: ")

try:
    video_id, items = get_api_information(url, apiKey)
except:
    print('Error at get_api_information')

try:
    videos_info = download_info(items)
    videos_caption = download_caption(video_id)
except:
    print('Error at downloading from items(json format)')

# videos_caption db에 title, defaultLanguage 추가
# you can handle which parameters will be included in caption table
for x in videos_caption:
    x.insert(0, videos_info[0])
    x.insert(1, videos_info[2])

# db 저장
try:
    insert_info(videos_info)
    insert_caption(videos_caption)
except:
    print('Error at storing db')
finally:
    close_connection()
