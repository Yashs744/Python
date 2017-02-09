import os
import zipfile
import re

# Pattern to search only .py extenion files
filePatter = re.compile(r'\.py|\.txt$')

# Creating Zip Object
newZip = zipfile.ZipFile('Python&Txt.zip', 'a')

for x, y, z in os.walk(os.getcwd()):
    for filename in z:
        if filePatter.search(filename):
            print('Compressing %s' % (filename))
            newZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
