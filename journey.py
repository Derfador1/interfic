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
		'up', 'enter cave', 
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
	answer = []
	
	while True:
		player.choose()

		os.system('clear')

		scene = a.Scene(winning_options[step], scene_descrip[random.randint(0, 3)])
		scene.create_treasure(step)
		
		scene.check_move(player)
		
		response = player.get_actions()
		
		if response == 'That was an incorrect option':
			print(response)
			continue
		
		if step == 0 or step == 3 or step == 13:
			if scene._action == 'move':
				print('You should probably get the things in this room before anything else')
				continue

		print(response)
		
		if scene._action == 'move':
			print('You have entered an area... ' + scene._description)

		if scene.get_winning_actions(player):
			print('that was correct option')
			answer.append(player._choice)
			step += 1
		else:		#could remove this to allow player to keep going to get to good path the round about way
			death = player.player_death()
			print(death)
			break
				
		if response == 'getting...' or 'taking...':
			player._lootbag.append(scene._item1)
			player._lootbag.append(scene._item2)
			
		if set(answer) == set(winning_options):
			print('winner winner chicken dinner')
			break
	

if __name__ == "__main__":
	main()
