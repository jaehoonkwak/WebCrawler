# WebCrawler
 for TDD Study
****

## _REQUIREMENTS:_


1. โ Input to the program: a list of urls (e.g., in a text file format)
   
    ๐ main/main.py _(#8)_
   

2. โ Retrieve the html contents from the specified web sites (ํด๋นํ๋ web site html์ ๋ค์ด๋ก๋) 
   
    ๐ main/main.py _(#12)_
   

3. โ Parse the html contents to extract hyperlinks (<href="...">) (html ์ค hyperlink ๋ถ๋ถ ์ถ์ถ)
   
    ๐ main/crawler.py _(#36)_
   

4. โ Crawl again from the parsed hyperlinks. (ํ์ฑํ url web site๋ฅผ ๋ค์ ๊ฐ์ ธ์ค๊ธฐ)
   
    ๐ main/crawler.py _(#46)_
   

5. โ Remove duplicates (ํ์ฑํ url list ์ค ์ค๋ณต ์ ๊ฑฐ)
   
    ๐ main/crawler.py _(#29)_

## _IF YOU RUN:_
~~~~
๐ What's the depth of crawling you need(in natural number): 2
[Download][SUCCESSโ] URL='http://www.google.com' to 'Downloads/0.html'
[Download][FAILโ] URL='http://www.naver.com' because of '<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1123)>'
[Download][SUCCESSโ] URL='http://www.google.com' to 'Downloads/1.html'
[Download][SUCCESSโ] URL='http://www.google.com' to 'Downloads/2.html'
๐ฆ Now crawling depth is: 1
  โ 'http://www.google.com' crawled ๐
  โ ๏ธ Unknown exception occurred in 'http://www.naver.com':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1123)>
๐ฆ Now crawling depth is: 2
  โ 'http://www.google.co.kr/imghp?hl=ko&tab=wi' crawled ๐
  โ ๏ธ Unknown exception occurred in 'http://maps.google.co.kr/maps?hl=ko&tab=wl':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
  โ ๏ธ Unknown exception occurred in 'http://www.youtube.com/?gl=KR&tab=w1':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
  โ ๏ธ Unknown exception occurred in 'http://www.google.co.kr/history/optout?hl=ko':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
  โ ๏ธ Unknown exception occurred in 'http://www.google.co.kr/intl/ko/services/':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
  โ 'http://www.google.com/setprefdomain?prefdom=KR&prev=http://www.google.co.kr/&sig=K_rQSbkXGj8GzsSnjt4Erk-OkvrDo%3D' crawled ๐


โ Crawling complete ๐
๐ Crawled URLs are (total=3): 
http://www.google.com
http://www.google.co.kr/imghp?hl=ko&tab=wi
http://www.google.com/setprefdomain?prefdom=KR&prev=http://www.google.co.kr/&sig=K_rQSbkXGj8GzsSnjt4Erk-OkvrDo%3D

๐ Bye~ ๐
