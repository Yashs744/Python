import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

website = 'https://www.google.co.in/maps/place/'

webbrowser.open(website+address)