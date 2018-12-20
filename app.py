import requests
from bs4 import BeautifulSoup as bs

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8"
        
#요청을 보내고 반응을 받는다.
res = requests.get(url).text
print(res)