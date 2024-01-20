# 패키지 설치
## pip show name // 패키지 내용 파악
## pip uninstall name // 패키지 삭제
## pip install --upgrade name // 패키지 업데이트

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())