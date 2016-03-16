#! /usr/bin/python3

import random
import time
import os
import area as a

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
	
	scene_descrip = [
		'You are on a hill!',
		'Stuff is in front of you',
		'You are stepping in poop',
		'I am looking at you'
		]

	#list_options = [
		#'light', 'examine', 
		#'get', 'take', 
		#'drop', 'put', 
		#'north', 'west', 
		#'south', 'east', 
		#'up', 'down', 
		#'wait', 'enter', 
		#'exit'
		#]
				
	#dict_choice = {'light':light, 'examine': examine, 'get':get, 'take':get, 'drop':drop}	
	
	step = 0
	
	player = a.Player()
	
	while True:
		player.choose()
		scene = a.Scene(winning_options[step], scene_descrip[random.randint(0, 3)])
		#make def in scene to give description if we have moved to the next scene
		print('You have entered a new area...: ' + scene._description)
		
		if scene.get_winning_actions(player):
			print('that was correct option')
			#create a new list
			step += 1
		else:
			death = player.player_death()
			print(death)
			break
		
		response = player.get_actions()
		print(response)

		#break
		#os.system('clear')
		#if input_choice == 'h':
			#menu = print_menu()
			#for item in menu:
				#print(item)
			
		#str1 = input_choice.split(' ')
		
		##make a cpital function so its all capital or is lower
		
		#for item in dict_choice:
			#if str1[0] == item:
				#output = dict_choice[item]()
				#print(output)


		#if not str1[0] in dict_choice:
			#if str1[0] == 'h':
				#continue
			#print('Fudge you')
		#step += 1
		
		
		#if input_choice == 'GET ALL':
			#if step != 1:
				#print('Not correct positon')
		#elif input_choice == 'OPEN DOOR':
			#if step < 2:
				#print('ew'')
		
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
		
		#if step == 20:
			#output = player_death()
			#print(output)
			#break



if __name__ == "__main__":
	main()
