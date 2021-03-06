import urllib
import re
import requests
from bs4 import BeautifulSoup


class Crawler:

    visited_urls = None
    crawl_need_depth = None
    crawl_current_depth = None

    def set(self, crawl_need_depth):
        self.visited_urls = []
        self.crawl_need_depth = crawl_need_depth
        self.crawl_current_depth = 0

    def crawl(self, urls):
        self.increase_crawl_current_depth()
        if self.crawl_current_depth > self.crawl_need_depth:
            print("\n\nโ Crawling complete ๐")
            return self.visited_urls

        print("๐ฆ Now crawling depth is: " + str(self.crawl_current_depth))

        new_urls = []
        for url in urls:
            # 5. โ Remove duplicates (ํ์ฑํ url list ์ค ์ค๋ณต ์ ๊ฑฐ)
            if url in self.visited_urls:
                continue

            try:
                html = urllib.request.urlopen(url)
                self.visited_urls.append(url)

                some_new_urls = self.extract_hyperlinks_from_html(html)
                new_urls.extend(some_new_urls)
                print("  โ '" + url + "' crawled ๐")
            except requests.exceptions.MissingSchema as e:
                print("  โ ๏ธ Invalid URL: " + str(e))
            except Exception as e:
                print("  โ ๏ธ Unknown exception occurred in '" + url + "':")
                print("      " + str(e))

        # 4. โ Crawl again from the parsed hyperlinks. (ํ์ฑํ url web site๋ฅผ ๋ค์ ๊ฐ์ ธ์ค๊ธฐ)
        return self.crawl(new_urls)

    def extract_hyperlinks_from_html(self, html):
        """
            3. โ Parse the html contents to extract hyperlinks (<href="...">) (html ์ค hyperlink ๋ถ๋ถ ์ถ์ถ)
        """
        soup = BeautifulSoup(html, "html.parser")
        result = soup.findAll('a', attrs={'href': re.compile("^http://")})

        return [url.get('href') for url in result]

    def increase_crawl_current_depth(self):
        self.crawl_current_depth = self.crawl_current_depth + 1
