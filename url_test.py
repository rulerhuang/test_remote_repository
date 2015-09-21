#!/usr/bin/env python
#encoding=utf-8

import os
import sys
import traceback
import chardet

from urllib2 import urlopen
from urllib2 import URLError
from urllib import quote
from lxml import etree


if __name__ == '__main__':
	data	= {}
	data_list	= []
	for age in xrange(1,5):
		data['age']	= age
		data_list.append(data)
		#data = {}
		#data_list.append(age)
	print data_list
