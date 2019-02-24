from bs4 import BeautifulSoup
from requests import get
import json

url, obj = input('Enter the url'), []
res = get(url).text
soup = BeautifulSoup(res, 'lxml')

channel_name = soup.select_one('.yt-user-info').getText().strip()
subscribers = soup.select_one('.yt-subscriber-count').getText()
published_date = soup.select_one('.watch-time-text').getText()
description = soup.select_one('#watch-description-text').text
views = round(int(''.join(i for i in soup.select_one('.watch-view-count').text if i.isdigit()))/ (10 ** 5), 2)
likes = int(''.join(i for i in soup.select_one('button[title="I like this"]').get_text() if i.isdigit()))
dislikes = int(''.join(i for i in soup.select_one('button[title="I dislike this"]').get_text() if i.isdigit()))

obj.append({'Channel_Name' : channel_name, 'Subscribers' : subscribers, 'published_date' : published_date,
            'Description' : description, 'Views' : views, 'Likes' : likes, 'Dislikes' : dislikes})

print(json.dumps(obj))
