import os
import shutil
import requests
from bs4 import BeautifulSoup

source = os.walk(os.getcwd())

for x,y,z in source:
	files = z
	break

for FILES in files:
	if FILES[-3:].lower() == 'txt':
		folder = 'Files'
		os.makedirs(folder, exist_ok=True)
		shutil.move('./' + FILES, './'+folder) 
