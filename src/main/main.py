from crawler import Crawler
from downloader import Downloader
from file_reader import get_urls


def main():
    # File Input
    start_urls = get_urls("src/main/input.txt")
    crawl_depth = int(input("👉 What's the depth of crawling you need(in natural number): "))

    # Download specified urls html
    Downloader.download(start_urls)

    # Crawl (urls html content)
    crawler = Crawler()
    crawler.set(crawl_depth)
    crawled_urls = crawler.crawl(start_urls)
    print("📈 Crawled URLs are (total=" + str(len(crawled_urls)) + "): ")
    for url in crawled_urls:
        print(url)
    print("\n👋 Bye~ 👋\n")


if __name__ == '__main__':
    main()
