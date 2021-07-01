#独学プログラマーのスクレイピング
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all('a'):
            url = tag.get('href')
            if url is None:
                continue
            if 'html' in url:
                print('\n' + url)

news = 'https://news.yahoo.co.jp/rss'
s = Scraper(news).scrape()

#with open ('scray.txt', 'w', encoding='utf-8') as f:
#    f.write(s)
    