#! /usr/bin/python3

import random
import time

random.seed(time.time())

def get():
	output = 'Getting...'
	return output
	
def light():
	output = 'Lighting...'
	return output
	
def player_death():
	random_list = [
		'giant rhinocerous with 12 horns!!', 
		'a falling stone you pleb!', 
		'tripping and falling on a rake that then flew up and hit a '
		'match which hit lit some dynamite which exploded',
		'seeing a squirrel and had a heart attack'
		]

def main():
	print('Welcome to the interactive fiction game')
	
	print('You have awoken in a strange cave there are 3 items in front of you')
	
	winning_options = [
		'get all', 'open door',
		'east', 'get edelweiss',
		'Up', 'enter cave', 
		'light fire', 'wait', 
		'put edelweiss in fire', 
		'put helmet in statue', 
		'put prism in pickle', 
		'exit cave', 'north', 
		'get meaning of life'
		]
		

	list_options = [
		'light', 'examine', 
		'get', 'take', 
		'drop', 'put', 
		'north', 'west', 
		'south', 'east', 
		'up', 'down', 
		'wait', 'enter', 
		'exit'
		]
				
	dict_choice = {'light':light, 'examine': examine, 'get':get, 'take':get, 'drop':drop}	
	
	step = 0
	
	while True:	
		input_choice = input('Enter a command: ')
		
		if input_choice == 'h':
			#menu = print_menu()
			#for item in menu:
			#	print(item)
			
		str1 = input_choice.split(' ')
		
		for item in list_options:
			if str1[0] == item:
				output = dict_choice[item]()
				print(output)

		#for item in list_option:
			#if item == input_choices:
				#player.item
			#else:
		
		#word = input_choice.split(' ')
		#for item in list_options
		#if word == item:
		#print('it is a valid option')
	
		#for item in winning_options:
			#if input_choice == item:
				#winning_options.remove(item)

		#print('printing list')
				
		#for item in winning_options:
			#print(item)
		
		
		#if len(winning_options) == 0:
			#print('We are done')
			#break
		#else:
			#print('Still things left')
			
		#if any(0 in dictionary)
		#keep going
		#else 
		#break because i am done
		
		if step == 20:
			output = player_death()
			print(output)
			break
		
		step += 1



if __name__ == "__main__":
	main()
