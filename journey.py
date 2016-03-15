#! /usr/bin/python3

import random
import time

random.seed(time.time())

def main():
	print('Welcome to the interactive fiction game')
	
	print('You have awoken in a strange cave there is a prism in front of you and a door to the north')
	
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



if __name__ == "__main__":
	main()
