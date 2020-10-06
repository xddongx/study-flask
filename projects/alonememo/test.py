from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient             # pymongo를 불러오라
client = MongoClient('localhost', 27017)    # localhost에 27017에 접근해라
db = client.dbsparta

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=167491'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']
print(title)
print(image)
print(desc)

