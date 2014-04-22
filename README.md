filescraper
===========

Scrapes a web page and downloads all linked files of specified file types. I wrote this to download lecture files from one of my class websites. For whatever reason, the professor will only keep up the 10 latest lecture documents, deleting old ones as he uploads new ones. Running this on cron ensures I never miss a file download.

### Usage
Example:

	csu:filescraper$ python scraper.py
	123Lecture01.pdf was already downloaded.
	123Lecture02.pdf was already downloaded.
	Worksheet-lec02.pdf was already downloaded.
	123Lecture03.pdf was already downloaded.
	123Lecture04.pdf was already downloaded.
	123Lecture05.pdf was already downloaded.
	123Lecture06.pdf was already downloaded.
	123Lecture07.pdf was already downloaded.
	123Lecture08.pdf was already downloaded.
	Downloaded: 123Lecture09.pdf
	Downloaded: Lecture10.doc
	csu:filescraper$