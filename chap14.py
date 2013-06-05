# This is where chapter 14 exercises go.
import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
	print line.strip()