#! python3
# debugCoinToss.py - Program to practice using debugging tools
# Program is purposefully made to be broken
# It is broken since the user enters heads or tails but the coin flip is represented by 0 or 1 
# It is also a bug that the coin flip value (0 or 1) is an integer and not a string

import random, logging

logging.basicConfig(filename = 'logging.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


logging.debug('Start of program\n-------------------')
guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails: ')
	guess = input()
logging.debug('User entered the value: ' + guess + '\nAnd is type of: ' + str(type(guess)))
toss = random.randint(0,1) # 0 is tails, 1 is heads
logging.debug('Value for coin flip: ' + str(toss) + '\nAnd is type of: ' + str(type(toss)))

logging.debug('Start if statement\n-------------------')
if(toss == guess):
	logging.debug('Guessed Right!')
	logging.debug('User entered the value: ' + guess + '\nAnd is type of: ' + str(type(guess)))
	logging.debug('Value for coin flip: ' + str(toss) + '\nAnd is type of: ' + str(type(toss)))
	print('You got it!')
else:
	logging.debug('Guessed Wrong!')
	logging.debug('User entered the value: ' + guess + '\nAnd is type of: ' + str(type(guess)))
	logging.debug('Value for coin flip: ' + str(toss) + '\nAnd is type of: ' + str(type(toss)))
	print('Nope! Guess again!')
	guess = input()
	
	if(toss == guess):
		logging.debug('Guessed Right!')
		logging.debug('User entered the value: ' + guess + '\nAnd is type of: ' + str(type(guess)))
		logging.debug('Value for coin flip: ' + str(toss) + '\nAnd is type of: ' + str(type(toss)))
		print('You got it!')
	else:
		logging.debug('Guessed Wrong Again!')
		logging.debug('User entered the value: ' + guess + '\nAnd is type of: ' + str(type(guess)))
		logging.debug('Value for coin flip: ' + str(toss) + '\nAnd is type of: ' + str(type(toss)))
		print('Nope. You are really bad at this game.')