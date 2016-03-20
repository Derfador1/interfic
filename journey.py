#! /usr/bin/python3

import random
import time
import os
import area as a
import sys
import signal

random.seed(time.time())

def print_menu():
	menu = [
		'opening menu...', 'Light x',
		'Examine', 'Get/Take x',
		'Drop x', 'Put x In y',
		'North x', 'West x',
		'South x', 'East x',
		'Up x', 'Down x',
		'Wait x', 'Enter x',
		'Exit x'
		]
	for item in menu:
		print(item)
	

def main():
	print('Welcome to the interactive fiction game')
	
	print('You have awoken from a deep sleep , begin playing or die?')
	print('Now you might be wondering , who the hell is talking to me right now!')
	print('Why the hell am I playing this game, I was just sipping coffee! Well')
	print('no longer, you are now playing this game and choose rightly or you')
	print('will die! (hint, "look" to see what is around)')
	print('(and "h" to open a menu of possible choices)')
	
	winning_options = [
		'get all', 'open door',
		'east', 'get edelweiss',
		'up', 'enter cave', 
		'light fire', 'wait', 
		'put edelweiss in fire', 
		'put helmet in statue', 
		'put prism in pickle', 
		'exit cave', 'north', 
		'get meaning of life'
		]

	scene_descrip = [
		'You have entered a cave!',
		'You are in a field',
		'You entered an archway and now you are standing in poo',
		'you entered a door, I am looking at you....but you dont see me'
		]
	
	step = 0
	
	player = a.Player()
	answer = []
	
	scene = a.Scene(winning_options[step], scene_descrip[random.randint(0, 3)])
		
	while True:
		#creates the treasure for the room
		scene.create_treasure(step)
		
		player.choose()
		os.system('clear')
		#checks if the choice was move choice or action choice						
		scene.check_move(player)
		
		response = player.get_actions()
		
		if response == 'h':
			print_menu()
			continue
		elif response == 'That was an incorrect option':
			print(response)
			continue
		elif response == 'Not in bag':
			print(response)
			continue
		elif response == 'looking...':
			print(response + '\n' + scene._description)
			#prints what objects are on the floor before you based on 2 items, 1 item, or no items
			if not scene._item1 == None and not scene._item2 == None:
				print('Before you is an', scene._item1)
				print('There is also a', scene._item2)
			elif scene._item1 == None and not scene._item2 == None:
				print('Before you is a', scene._item2)
			elif scene._item2 == None and not scene._item1 == None:
				print('Before you is a', scene._item1)
			else:
				print('No items')
				
			continue
		
		if step == 0 or step == 3 or step == 13:
			if scene._action == 'move':
				print('You should probably get the things in this room before anything else')
				continue
				
		print(response)
					
		if response == 'getting...':
			#prints what was got depending on 2 items , 1 item, or no items
			player._lootbag.append(scene._item1)
			player._lootbag.append(scene._item2)
			
			if not scene._item1 == None:
				print(scene._item1)
			if not scene._item2 == None:
				print(scene._item2)
				
			scene._item1 = None
			scene._item2 = None
		
		if scene.get_winning_actions(player):
			print('That was the only correct option!')
			answer.append(player._choice)
			#increase step except for the last one
			if step < 13:
				step += 1
				
			if scene._action == 'move':
				scene = a.Scene(winning_options[step], scene_descrip[random.randint(0, 3)])
			else:
				#updates scene instead of creating a new one
				scene.scene_update(winning_options[step])

		else:		#could remove this to allow player to keep going to get to good path the round about way
			death = player.player_death()
			print(death)
			break
		
		#mathces if answer and winning options are the same
		if set(answer) == set(winning_options):
			print('you have won')
			break
	

if __name__ == "__main__":
	try:
		main()
	#catches the keyboard interrupt if ^C is used to end program
	except KeyboardInterrupt:
		print('\nInterrupted...')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
