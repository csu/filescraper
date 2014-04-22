import urllib2
import urlparse
import os
import BeautifulSoup
import config

request = urllib2.Request(config.LINK_TO_SCRAPE)
response = urllib2.urlopen(request)
soup = BeautifulSoup.BeautifulSoup(response)

for a in soup.findAll('a'):
	filename = a['href']
	if not os.path.isfile(filename): # don't download something twice
		url = config.FILE_BASE + filename
		path = urlparse.urlparse(url).path
		ext = os.path.splitext(path)[1]
		if ext in config.FILE_TYPES:
			file = urllib2.urlopen(url)
			output = open(filename,'wb')
			output.write(file.read())
			output.close()
			print 'Downloaded: ' + filename
	else:
		print filename + " was already downloaded."