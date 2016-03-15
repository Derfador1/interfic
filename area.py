#! /usr/bin/python3

import random
import time

random.seed(time.time())

class Map:
	def __init__(self):
		self._list1 = []
	
	def create_options(self):	
		random_dir = ['North', 'South', 'East', 'West', 'Up', 'Down']
		for item in random_dir:
			random_int = random.randint(0,1)
			if random_int == 1:
				list1.append(item)
	
class Item:
	#generate items
