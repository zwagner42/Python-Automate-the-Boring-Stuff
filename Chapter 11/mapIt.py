#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip

#Usage message
print("Usage:  mapIt <street>, <city>, <state> <zipcode>")
print("Example: mapIt 870 Valencia St, San Francisco, CA 94110\n")
print("Also will use an address copied into the clipboard with ctrl+C.\n")

if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])
else:
	#Get address from clipboard
	addresss = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)