from bs4 import BeautifulSoup
from requests import get
import argparse
import pprint

parser = argparse.ArgumentParser(add_help=False, description=('Download reviews from BookMyShow'))
parser.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
parser.add_argument('--youtube_url', '-yt', help='Enter Url extract reviews')
args = parser.parse_args()

res = get(args.youtube_url).text
soup = BeautifulSoup(res, 'lxml')

channel_name = soup.select_one('.yt-user-info').getText().strip()
subscribers = soup.select_one('.yt-subscriber-count').getText()
published_date = soup.select_one('.watch-time-text').getText()
description = soup.select_one('#watch-description-text').text
views = round(int(''.join(i for i in soup.select_one('.watch-view-count').text if i.isdigit()))/ (10 ** 5), 2)
likes = int(''.join(i for i in soup.select_one('button[title="I like this"]').get_text() if i.isdigit()))
dislikes = int(''.join(i for i in soup.select_one('button[title="I dislike this"]').get_text() if i.isdigit()))

pprint.pprint({'Channel_Name' : channel_name, 'Subscribers' : subscribers,
'published_date' : published_date, 'Description' : description,
'Views' : views, 'Likes' : likes, 'Dislikes' : dislikes})
