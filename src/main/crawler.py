import requests
from bs4 import BeautifulSoup


class Crawler:
    @staticmethod
    def crawl(urls):
        htmls = []
        for url in urls:
            try:
                html = requests.get(url)
                htmls.append(html)
            except requests.exceptions.MissingSchema as e:
                print("Invalid URL:" + str(e))
                
        return htmls
