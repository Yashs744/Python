import requests
import sys
import webbrowser
import bs4
import argparse

parser = argparse.ArgumentParser(description="Search Google and Open's Top 5 Result in Different Tabs")
parser.add_argument('search', metavar='keyword', type=str, nargs='+',
			help='Keyword to Search')

args = parser.parse_args()

def GoogleSearch():
	base_url = 'http://google.com/search?q='
	print('Googling...')

	res = requests.get(base_url + ' '.join(sys.argv[1:]))
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, "lxml")

	linkElems = soup.select('.r a')

	numOpen = min(5, len(linkElems))
	for i in range(numOpen):
		webbrowser.open('http://google.com' + linkElems[i].get('href'))

GoogleSearch()
