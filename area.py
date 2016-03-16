#! /usr/bin/python3

import random
import time
import journey as j

random.seed(time.time())

	
def get():
	output = 'getting...'
	return output
	
def light():
	output = 'lighting...'
	return output
	
def drop():
	output = 'dropping things...'
	return output
	
def examine():
	output = 'examining...'
	return output
	
def open():
	output = 'opening...'
	return output

def north():
	output = 'going north...'
	return output

def open1():
	output = 'opening...'
	return output
	
def west():
	output = 'going west...'
	return output

def east():
	output = 'going east...'
	return output

def south():
	output = 'going south...'
	return output
	
def up():
	output = 'going up...'
	return output
	
def down():
	output = 'going down...'
	return output

def enter():
	output = 'entering...'
	return output
	
def exit1():
	output = 'exiting...'
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


action_dict = {'light':light, 'examine': examine, 'get':get, 'take':get, 'drop':drop}
move_dict = {'north':north, 'open':open1, 'west':west, 'east':east, 'south':south, 'up':up, 'down':down, 'enter':enter, 'exit':exit1}

class Game:
	def __init__(self, winning_action):
		self._winning_action = winning_action
		self._action = None
		
	def get_actions(self):
		str1 = self._choice.split(' ')
	
		if not str1[0] in move_dict:
			for item in action_dict:
				if str1[0] == item:
					output = action_dict[item]()
					return(output)
		else:
			for item in move_dict:
				if str1[0] == item:
					output = move_dict[item]()
					return(output)
	
			
		if not str1[0] in move_dict or action_dict:
			output = 'Fudge you'
			if str1[0] == 'h':
				menu = print_menu()
				return(menu)
			return(output)

	def get_winning_actions(self, other):
		if other._choice == self._winning_action:
			return True
		return False

	def check_move(self, other):
		str1 = other._choice.split(' ')		
		
		if not str1[0] in move_dict:
			print('here1')
			self._action = 'action'
		else:
			print('here2')
			self._action = 'move'
		

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
			'match which lit some dynamite which exploded',
			'seeing a squirrel and having a heart attack'
			]
			
		output = 'You were killed by ' + random_list[random.randint(0, 3)]
			
		return(output)
		
class Scene(Game):
	def __init__(self, winning_action, description):
		super().__init__(winning_action)
		self._description = description
		self._item1 = None
		self._item2 = None
		
	def create_treasure(self, step):
		if step == 0:
			self._item1 = 'Helmet'
			self._item2 = 'Prism'
		elif step == 3:
			self._item1 = 'Edelweiss'
		
		
		

			
	
