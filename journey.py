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
		'Examine x', 'Get/Take x',
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
	
	while True:
		player.choose()

		os.system('clear')

		scene = a.Scene(winning_options[step], scene_descrip[random.randint(0, 3)])
		scene.create_treasure(step)
		
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
		elif response == 'examining...':
			print(response + '\n' + scene._description)
			continue
		
		if step == 0 or step == 3 or step == 13:
			if scene._action == 'move':
				print('You should probably get the things in this room before anything else')
				continue
				
		print(response)
					
		if response == 'getting...':
			player._lootbag.append(scene._item1)
			player._lootbag.append(scene._item2)
			
			if not scene._item1 == None:
				print(scene._item1)
			if not scene._item2 == None:
				print(scene._item2)
		
		#if scene._action == 'move':
			#print('You have entered an area...' + scene._description)

		if scene.get_winning_actions(player):
			print('that was the correct option')
			answer.append(player._choice)
			step += 1
		else:		#could remove this to allow player to keep going to get to good path the round about way
			death = player.player_death()
			print(death)
			break
			
		if set(answer) == set(winning_options):
			print('you have won')
			break
	

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print('\nInterrupted...')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
