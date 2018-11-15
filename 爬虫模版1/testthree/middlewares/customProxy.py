#!/usr/bin/env python
#-*- coding: utf-8 -*-



from testthree.middlewares.resource import PROXIES
import random

class RandomProxy(object):
	def process_request(self,request,spider):
		proxy = random.choice(PROXIES)
		# request.meta['proxy'] = 'http://%s' %proxy
		try:
			print("当前的IP是：" + proxy)
			request.meta["proxy"] = 'http://%s' %proxy
		except Exception as e:
			print(e)
			pass