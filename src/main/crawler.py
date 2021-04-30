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
            print("\n\n✅ Crawling complete 👍")
            return self.visited_urls

        print("🔦 Now crawling depth is: " + str(self.crawl_current_depth))

        new_urls = []
        for url in urls:
            # 5. ✅ Remove duplicates (파싱한 url list 중 중복 제거)
            if url in self.visited_urls:
                continue

            try:
                html = urllib.request.urlopen(url)
                self.visited_urls.append(url)

                some_new_urls = self.extract_hyperlinks_from_html(html)
                new_urls.extend(some_new_urls)
                print("  ✅ '" + url + "' crawled 👏")
            except requests.exceptions.MissingSchema as e:
                print("  ⚠️ Invalid URL: " + str(e))
            except Exception as e:
                print("  ⚠️ Unknown exception occurred in '" + url + "':")
                print("      " + str(e))

        # 4. ✅ Crawl again from the parsed hyperlinks. (파싱한 url web site를 다시 가져오기)
        return self.crawl(new_urls)

    def extract_hyperlinks_from_html(self, html):
        """
            3. ✅ Parse the html contents to extract hyperlinks (<href="...">) (html 중 hyperlink 부분 추출)
        """
        soup = BeautifulSoup(html, "html.parser")
        result = soup.findAll('a', attrs={'href': re.compile("^http://")})

        return [url.get('href') for url in result]

    def increase_crawl_current_depth(self):
        self.crawl_current_depth = self.crawl_current_depth + 1
