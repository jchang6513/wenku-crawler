import os
import requests
from bs4 import BeautifulSoup
from opencc import OpenCC

cc = OpenCC('s2t')
cc.set_conversion('s2tw')

aid = '2321'
url = 'https://m.linovelib.com/novel/'+aid+'/catalog'

r = requests.get(url)
#r.encoding = "gbk"
soup = BeautifulSoup(r.text, 'html.parser')
title = cc.convert(soup.find("h1",{"class":"header-back-title"}).getText())
lis = soup.find_all("li")

if os.path.exists(title) == False:
	os.mkdir(title)

for li in lis:
	if li['class'][0] == 'chapter-bar':
		try:
			f.close()
		except KeyboardInterrupt:
			sys.exit()
		except Exception as e:
		    print(e)
		book_name = title+' '+cc.convert(li.get_text())
		f = open(title+'/'+book_name+'.txt','w')
	else:
		chapter_name = cc.convert(li.get_text())
		print(chapter_name)
		f.write('<chapter>'+chapter_name+'</chapter>\n')

		try:
			ch = requests.get('https://m.linovelib.com/'+li.find("a")['href'])
			#ch.encoding = "gbk"
			soup = BeautifulSoup(ch.text, 'html.parser')
			content = cc.convert(soup.find("div",{"id":"acontent"}).getText())
			f.write(content)
		except KeyboardInterrupt:
			sys.exit()
		except Exception as e:
		    print(e)


















		#
