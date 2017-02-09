import os
import shutil

source = os.walk(os.getcwd())

for x,y,z in source:
	files = z
	break

for FILES in files:
	if FILES[-3:].lower() == 'txt' or FILES[-3:].lower() == 'pdf':
		folder = 'Files'
		os.makedirs(folder, exist_ok=True)
		shutil.move('./' + FILES, './'+folder)
