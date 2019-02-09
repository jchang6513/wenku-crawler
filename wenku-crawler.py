# import scrapy
#
# class ArticlesSpider(scrapy.Spider):
#     name = "articles"
#     start_urls = [
#         'https://www.wenku8.net/modules/article/reader.php?aid=1787',
#     ]
#
#     def parse(self, response):
#         for article in response.css('td.ccss'):
#             yield {
#                 'title': article.css('a::text').extract_first(),
#                 'link': article.css('a::attr("href")').extract_first(),
#             }

import os
import requests
from bs4 import BeautifulSoup
from opencc import OpenCC

cc = OpenCC('s2t')
cc.set_conversion('s2tw')

# aid = input('請輸入小說aid: ')
aid = '1787'
url = 'https://www.wenku8.net/modules/article/reader.php?aid='+aid

r = requests.get(url)
r.encoding = "gbk"
soup = BeautifulSoup(r.text, 'html.parser')
title = cc.convert(soup.find("div",{"id":"title"}).getText())
tds = soup.find_all("td")

if os.path.exists(title) == False:
	os.mkdir(title)

for td in tds:
	if td['class'][0] == 'vcss':
		try:
			f.close()
		except KeyboardInterrupt:
			sys.exit()
		except Exception as e:
		    print(e)
		book_name = title+' '+cc.convert(td.get_text())
		f = open(title+'/'+book_name+'.txt','w')
	else:
		chapter_name = cc.convert(td.get_text())
		print(chapter_name)
		f.write(chapter_name+'\n')

		try:
			ch = requests.get(td.find("a")['href'])
			ch.encoding = "gbk"
			soup = BeautifulSoup(ch.text, 'html.parser')
			content = cc.convert(soup.find("div",{"id":"content"}).getText())
			f.write(content)
		except KeyboardInterrupt:
			sys.exit()
		except Exception as e:
		    print(e)

































		#
