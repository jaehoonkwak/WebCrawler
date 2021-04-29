from crawler import Crawler
from file_reader import get_urls
import os

if __name__ == '__main__':
    path = os.getcwd()
    urls = get_urls("src/main/input.txt")

    Crawler.crawl(urls)
