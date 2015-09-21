#!/usr/bin/env python
#encoding=utf-8

import yaml

if __name__ == '__main__':
	with open('markets_and_apps.yaml','r') as fd:
		markets	= yaml.load(fd)
	for market_name,market_details in markets.items():
		for category,details in market_details.items():
			for detail in details:
				parent_category	= detail.get('parent_category')
				child_category	= detail.get('child_category')
				url				= detail.get('url')
				print	market_name,category,parent_category,child_category,url
			

