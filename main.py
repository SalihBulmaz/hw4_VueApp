import json
from curses.ascii import BEL
import requests
from bs4 import BeautifulSoup
hackernews = []
for page in range(1, 5):
    soup = BeautifulSoup(requests.get(f'https://news.ycombinator.com/news?p={page}').content, "html.parser")
    for anchor_tag in soup.find_all(class_ = 'titlelink'):
        hackernews.append(anchor_tag.attrs["href"])
print(json.dumps(hackernews))