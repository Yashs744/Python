#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
import os
import datetime
from time import sleep
import sys

dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)

while True:
	os.makedirs('MyBing', exist_ok=True)
	url = 'http://bingwallpaper.com/'
	sc = requests.get(url)
	soup = BeautifulSoup(sc.text, 'lxml')
	image = soup.select('.cursor_zoom img')
	image_url = image[0].get('src')
	res = requests.get(image_url)

	with open(os.path.join('MyBing', cd+'.txt'), 'w') as f:
		f.write('soup: '+str(soup))
		f.write("\n\n")
		f.write('image: '+str(image))
		f.write("\n\n")
		f.write('image_url: '+str(image_url))

	with open(os.path.join('MyBing', cd+'.jpg'), 'wb') as file:
		file.write(res.content)
	
	os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/Documents/web_crawlers/MyBing/'+cd+'.jpg')
	
	break;
sys.exit()
