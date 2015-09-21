#!/usr/bin/env python
#encoding=utf-8

import os
import sys
import time
import yaml
import chardet
import traceback

from urllib import quote
from urllib2 import Request
from urllib2 import urlopen
from lxml import etree


def get_web_info(url,safe=':/?=&#'):
	try:
		if isinstance(url,unicode):
			url	= url.encode('utf-8')

		url = quote(url,safe=safe)
		print	url
		user_agent 	= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers		= {'User-Agent':user_agent}
		req	= Request(url=url,headers=headers)
		fd	= urlopen(req)
		web_info	= fd.read()
		if chardet.detect(web_info)['encoding'] == 'utf-8':
			web_info	= web_info.decode('utf-8')

		fd.close()
	except Exception:
		print	traceback.format_exc()
		web_info	= None
	return	web_info


def get_wandoujia_program_name(url,category):
	program_name_list	 = []
	for page_num in xrange(1,2):
		page_url = url + str(page_num)
		web_info	= get_web_info(page_url)
		if web_info is not None:
			tree	= etree.HTML(web_info)
			if category == 'apps':
				AppInfo = etree.XPath('/html/body//div[@class="container"]//ul[@class="app-box clearfix"]//li//div[@class="app-desc"]/a/text()')(tree)
			else:
				AppInfo = etree.XPath('/html/body//div[@class="app-block-wp"]/ul//li//div[@class="desc"]/a[@class="title name popup-area"]/text()')(tree)

			for program_name in AppInfo:
				try:
					print	program_name
					program_name_list.append(program_name.strip())
				except Exception:
					print	'GET_WANDOUJIA_PROGRAM_NAME FAILD'
					print	traceback.format_exc()
					print	url
		else:
			print	'WEB_INFO_IS_NONE:',page_url
	return program_name_list


def get_360_program_name(url):
	program_name_list	 = []
	for page_num in xrange(1,2):
		page_url = url + '?page=' + str(page_num)
		web_info	= get_web_info(page_url)
		if web_info is not None:
			tree	= etree.HTML(web_info)
			AppInfo = etree.XPath('/html/body//div[@class="icon_box"]//ul[@class="iconList"]//li/h3/a/text()')(tree)
			for app_info in AppInfo:
				try:
					program_name = app_info
					print	program_name
					program_name_list.append(program_name.strip())
				except Exception:
					print	'GET_360_PROGRAM_NAME FAILD'
					print	tracebak.format_exc()
					print	url
		else:
			print	'WEB_INFO_IS_NONE:',page_url
	return program_name_list


def get_xiaomi_program_name(url):
	program_name_list	 = []
	for page_num in xrange(1,3):
		page_url	= url + '#page=' + str(page_num)
		web_info	= get_web_info(page_url)
		if web_info is not None:
			tree	= etree.HTML(web_info)
			AppInfo = etree.XPath('/html/body//div[@class="applist-wrap"]//ul[@id="all-applist"]//li/h5/a/text()')(tree)
			for app_info in AppInfo:
				try:
					program_name	= app_info
					print	program_name
					program_name_list.append(program_name.strip())
				except Exception:
					print 'GET_XIAOMI_PROGRAM_NAME FAILD'
					print	traceback.format_exc()
					print	page_url
	return program_name_list 


def get_baidu_program_name(url):
	program_name_list	 = []
	for page_num in xrange(1,2):
		page_url	= url + '&page_num=' + str(page_num)
		web_info	= get_web_info(page_url)
		if web_info is not None:
			tree	= etree.HTML(web_info)
			AppInfo = etree.XPath('/html/body//div[@class="list-bd app-bd"]//ul//li//div[@class="app-meta"]/p[@class="name"]/text()')(tree)
			for app_info in AppInfo:
				try:
					program_name	= app_info
					print	program_name
					program_name_list.append(program_name.strip())
				except Exception:
					print 'GET_XIAOMI_PROGRAM_NAME FAILD'
					print	traceback.format_exc()
					print	page_url
	return program_name_list 


def get_app_qq_program_name(url):
	program_name_list	 = []
	page_url	= url 
	web_info	= get_web_info(page_url)
	if web_info is not None:
		tree	= etree.HTML(web_info)
		AppInfo = etree.XPath('/html/body//div[@class="mod-app-container"]/ul//li//div[@class="app-content"]/h3/text()')(tree)
		for app_info in AppInfo:
			try:
				program_name	= app_info
				print	program_name
				program_name_list.append(program_name.strip())
			except Exception:
				print 'GET_XIAOMI_PROGRAM_NAME FAILD'
				print	traceback.format_exc()
				print	page_url
	return program_name_list 


def get_anzhi_program_name(url,category):
	program_name_list	 = []
	for page_num in xrange(1,2):
		if category == 'apps':
			page_url	= url + str(page_num) + '_hot.html'
		else:
			page_url	= url + str(page_num) + '_new.html'

		web_info	= get_web_info(page_url)
		if web_info is not None:
			tree	= etree.HTML(web_info)
			AppInfo = etree.XPath('/html/body//div[@class="app_list border_three"]/ul//li//div[@class="app_info"]/span/a/text()')(tree)
			for app_info in AppInfo:
				try:
					program_name	= app_info
					print	program_name
					program_name_list.append(program_name.strip())
				except Exception:
					print 'GET_XIAOMI_PROGRAM_NAME FAILD'
					print	traceback.format_exc()
					print	page_url
	return program_name_list 


def get_hiapk_program_name(url):
	program_name_list	 = []
	for page_num in xrange(1,2):
		page_url	= url + '?sort=5&pi=' + str(page_num) 
		web_info	= get_web_info(page_url)
		if web_info is not None:
			tree	= etree.HTML(web_info)
			AppInfo = etree.XPath('/html/body//div[@class="soft_list_box"]/ul//li//span[@class="list_title font14_2"]/a/text()')(tree)
			for app_info in AppInfo:
				try:
					program_name	= app_info
					print	program_name
					program_name_list.append(program_name.strip())
				except Exception:
					print 'GET_XIAOMI_PROGRAM_NAME FAILD'
					print	traceback.format_exc()
					print	page_url
	return program_name_list 



if __name__ == '__main__':
	try:
		markets = 'markets_and_apps.yaml'
		with open(markets,'rb') as fd:
			markets	= yaml.load(fd)
		
		for market_name,market_details in markets.items():
			for category,details in market_details.items():
				for detail in details:
					market_name		= market_name
					parent_category	= detail.get('parent_categroy')
					child_categroy	= detail.get('child_categroy')
					url				= detail.get('url')
					#print market_name,category,parent_category,child_categroy,url
					
					program_name_list = []
					if market_name == u'豌豆荚':
						pass
						#program_name_list	= get_wandoujia_program_name(url,category)
					elif market_name == u'360手机助手':
						pass
						#program_name_list	 = get_360_program_name(url)
					elif market_name == u'小米应用商店':
						pass
						#program_name_list	 = get_xiaomi_program_name(url)
					elif market_name == u'百度手机助手':
						pass
						#program_name_list	 = get_baidu_program_name(url)
					elif market_name == u'应用宝':
						pass
						program_name_list	 = get_app_qq_program_name(url)
					elif market_name == u'安智':
						pass
						#program_name_list	 = get_anzhi_program_name(url,category)
					elif market_name == u'安卓市场':
						pass
						#program_name_list	 = get_hiapk_program_name(url)
	except KeyboardInterrupt:
		print	'get keyboard'
		raise KeyboardInterrupt
	except Exception:
		print	traceback.format_exc()
