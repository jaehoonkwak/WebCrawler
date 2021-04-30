# WebCrawler
 for TDD Study
****

## _REQUIREMENTS:_


1. ✅ Input to the program: a list of urls (e.g., in a text file format)
   
    👉 main/main.py _(#9)_
   

2. ✅ Retrieve the html contents from the specified web sites (해당하는 web site html을 다운로드) 
   
    👉 main/main.py _(#13)_
   

3. ✅ Parse the html contents to extract hyperlinks (<href="...">) (html 중 hyperlink 부분 추출)
   
    👉 main/crawler.py _(#27)_
   

4. ✅ Crawl again from the parsed hyperlinks. (파싱한 url web site를 다시 가져오기)
   
    👉 main/crawler.py _(#37)_
   

5. ✅ Remove duplicates (파싱한 url list 중 중복 제거)
   
    👉 main/crawler.py _(#18)_

## _IF YOU RUN:_
~~~~
👉 What's the depth of crawling you need(in natural number): 2
[Download][SUCCESS✅] URL='http://www.google.com' to 'Downloads/0.html'
[Download][FAIL❌] URL='http://www.naver.com' because of '<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1123)>'
[Download][SUCCESS✅] URL='http://www.google.com' to 'Downloads/1.html'
[Download][SUCCESS✅] URL='http://www.google.com' to 'Downloads/2.html'
🔦 Now crawling depth is: 1
  ✅ 'http://www.google.com' crawled 👏
  ⚠️ Unknown exception occurred in 'http://www.naver.com':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1123)>
🔦 Now crawling depth is: 2
  ✅ 'http://www.google.co.kr/imghp?hl=ko&tab=wi' crawled 👏
  ⚠️ Unknown exception occurred in 'http://maps.google.co.kr/maps?hl=ko&tab=wl':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
  ⚠️ Unknown exception occurred in 'http://www.youtube.com/?gl=KR&tab=w1':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
  ⚠️ Unknown exception occurred in 'http://www.google.co.kr/history/optout?hl=ko':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
  ⚠️ Unknown exception occurred in 'http://www.google.co.kr/intl/ko/services/':
      <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)>
  ✅ 'http://www.google.com/setprefdomain?prefdom=KR&prev=http://www.google.co.kr/&sig=K_rQSbkXGj8GzsSnjt4Erk-OkvrDo%3D' crawled 👏


✅ Crawling complete 👍
📈 Crawled URLs are (total=3): 
http://www.google.com
http://www.google.co.kr/imghp?hl=ko&tab=wi
http://www.google.com/setprefdomain?prefdom=KR&prev=http://www.google.co.kr/&sig=K_rQSbkXGj8GzsSnjt4Erk-OkvrDo%3D

👋 Bye~ 👋
