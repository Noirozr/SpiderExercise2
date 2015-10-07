#!/usr/bin/python
# Python Spider Exercise 2
# written by Osiris

import sys
import re
import urllib2
import HTMLParser

class myparser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		
	def handle_starttag(self, tag, attrs):
		if (tag == 'a') | (tag == 'img'):
			for name, value in attrs:
				if (name == 'href') | (name == 'arc'):
					val = re.search('http://', value)
					if val != None:
						print value
						
if sys.argv[1] == '-u':
	content = (urllib2.urlopen(sys.argv[2])).read()
	con = myparser()
	con.feed(content)
else:
	print 'Usage:%s -u url'%sys.argv[0] 


