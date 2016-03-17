#! /usr/bin/python3

import random
import time
import journey as j

random.seed(time.time())
	
def get(self):
	output = 'getting...'
	return output
	
def wait(self):
	output = 'waiting...'
	return output

def put(self):
	str1 = self._choice.split(' ')

	x = str1[1]
	y = str1[3]
	
	if x in self._lootbag:
		if x == x or x == y:
			self._lootbag.remove(x)

	output = 'putting...' + x + ' in ' + y
	return output
	
def light(self):
	output = 'lighting...' 
	return output
	
def drop(self):
	str1 = self._choice.split(' ')

	x = str1[1]

	output = 'Not in bag'

	for item in self._lootbag:
		if item == x:
			print('here')
			self._lootbag.remove(x)
			output = 'dropping ' + x + '...'
			
	return output
	
def examine(self):
	output = 'examining...'
	return output

def north(self):
	output = 'going north...'
	return output

def open1(self):
	output = 'opening...'
	return output
	
def west(self):
	output = 'going west...'
	return output

def east(self):
	output = 'going east...'
	return output

def south(self):
	output = 'going south...'
	return output
	
def up(self):
	output = 'going up...'
	return output
	
def down(self):
	output = 'going down...'
	return output

def enter(self):
	output = 'entering...'
	return output
	
def exit1(self):
	output = 'exiting...'
	return output


action_dict = {'light':light, 'examine': examine, 'get':get, 'take':get, 'drop':drop, 'wait':wait, 'put':put}
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
					output = action_dict[item](self)
					return(output)
		elif not str1[0] in action_dict:
			for item in move_dict:
				if str1[0] == item:
					output = move_dict[item](self)
					return(output)
	
		if not str1[0] in move_dict or action_dict:
			output = 'That was an incorrect option'
			if str1[0] == 'h':
				menu = 'h'
				return menu
			return(output)

	def get_winning_actions(self, other):
		if other._choice == self._winning_action:
			return True
		return False

	def check_move(self, other):
		str1 = other._choice.split(' ')		
		
		if not str1[0] in move_dict:
			self._action = 'action'
		else:
			self._action = 'move'
		

class Player(Game):
	def __init__(self):
		super().__init__(None)
		self._lootbag = []
		self._choice = None

	def choose(self):
		self._choice = input('Enter a command: ')
		self._choice = self._choice.lower()
		
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
			self._item1 = 'helmet'
			self._item2 = 'prism'
		elif step == 3:
			self._item1 = 'edelweiss'
		elif step == 13:
			self._item = 'meaning of life'
		
		
		

			
	
