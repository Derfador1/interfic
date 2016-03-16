#! /usr/bin/python3

import random
import time
import os
import area as a

random.seed(time.time())

def main():
	print('Welcome to the interactive fiction game')
	
	print('You have awoken in a strange cave there are items in front of you : ')
	
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
	
	scene_descrip = [
		'You are on a hill!',
		'Stuff is in front of you',
		'You are stepping in poop',
		'I am looking at you'
		]
	
	step = 0
	
	player = a.Player()
	
	while True:
		player.choose()
		scene = a.Scene(winning_options[step], scene_descrip[random.randint(0, 3)])
		scene.create_treasure(step)
		
		scene.check_move(player)
		
		if scene._action == 'move':
			print('You have entered an area... ' + scene._description)
		
		if scene.get_winning_actions(player):
			print('that was correct option')
			#create a new list
			step += 1
		else:
			death = player.player_death()
			print(death)
			break
		
		response = player.get_actions()
		
		if response == 'getting...' or 'taking...':
			player._lootbag.append(scene._item1)
			player._lootbag.append(scene._item2)
	
		print(response)


if __name__ == "__main__":
	main()
