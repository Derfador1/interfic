#! /usr/bin/python3

import random
import time
import journey as j

random.seed(time.time())

	
def get():
	output = 'Getting...'
	return output
	
def light():
	output = 'Lighting...'
	return output
	
def drop():
	output = 'Dropping things...'
	return output
	
def examine():
	output = 'examining...'
	return output
	
def open():
	output = 'opening...'
	return output

def print_menu():
	menu = [
		'opening menu...', 'Light x',
		'Examine x', 'Get/Take x',
		'Drop x', 'Put x In y',
		'North x', 'West x',
		'South x', 'East x',
		'Up x', 'Down x',
		'Wait x', 'Enter x',
		'Exit x'
		]
	return menu

dict_choice = {'light':light, 'examine': examine, 'get':get, 'take':get, 'drop':drop}

class Game:
	def __init__(self, winning_action):
		self._winning_action = winning_action
		
	def get_actions(self):
		str1 = self._choice.split(' ')
	
		for item in dict_choice:
			if str1[0] == item:
				output = dict_choice[item]()
				return(output)
			
		if not str1[0] in dict_choice:
			output = 'Fudge you'
			if str1[0] == 'h':
				menu = print_menu()
				return(menu)
			return(output)

	def get_winning_actions(self, other):
		if other._choice == self._winning_action:
			return True
		return False
		

class Player(Game):
	def __init__(self):
		super().__init__(None)
		self._lootbag = []
		self._choice = None

	def choose(self):
		self._choice = input('Enter a command: ')
		
	def player_death(self):
		random_list = [
			'a giant rhinocerous with 12 horns!!', 
			'a falling stone you pleb!', 
			'tripping and falling on a rake that then flew up and hit a '
			'match which hit lit some dynamite which exploded',
			'seeing a squirrel and having a heart attack'
			]
			
		output = 'You were killed by ' + random_list[random.randint(0, 3)]
			
		return(output)
		
class Scene(Game):
	def __init__(self, winning_action, description):
		super().__init__(winning_action)
		self._description = description
		
	
		

			
	
