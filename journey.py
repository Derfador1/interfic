#! /usr/bin/python3

import random
import time

random.seed(time.time())

def main():
	print('Welcome to the interactive fiction game')
	
	print('You have awoken in a strange cave there is a prism in front of you and a door to the north')
	
	winning_options = [
				'get all', 'open door',
				'east', 'get edelweiss',
				'Up', 'Enter cave', 
				'Light fire', 'Wait', 
				'Put edelweiss in fire', 
				'Put helmet in statue', 
				'Put prism in pickle', 
				'Exit cave', 'North', 
				'Get meaning of life'
				]
				

	list_options = [
				'Light', 'Examine', 
				'Get', 'Take', 
				'Drop', 'Put', 
				'North', 'West', 
				'South', 'East', 
				'Up', 'Down', 
				'Wait', 'Enter', 
				'Exit'
				]
	
	while True:
	
		input_choice = input('Enter a command: ')
		
		if input_choice == 'h':
			print('opening menu...')
			
			print('Light x')
			print('Examine x')
			print('Get/Take x')
			print('Drop x')
			print('Put x In y')
			print('North x')
			print('West x')
			print('South x')
			print('East x')
			print('Up x')
			print('Down x')
			print('Wait x')
			print('Enter x')
			print('Exit x')	
			
	
		for item in winning_options:
			if input_choice == item:
				winning_options.remove(item)

		print('printing list')
				
		for item in winning_options:
			print(item)
		
		
		if len(winning_options) == 0:
			print('We are done')
			break
		else:
			print('Still things left')



if __name__ == "__main__":
	main()
