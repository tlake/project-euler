import math

#this is gonna be the dumb, first, but hopefully more or less
#effective brute force tanner method

#someday I hope to be able to skip this first step and just
#generate a one-level-more-elegant version at the start.

def nth_prime(goal):
	#start counting up numbers
	number = 1
	prime_counter = 0
	#for each number, test if it's prime
	#if it is, add one to the prime counter
	while prime_counter != goal:
		number += 1
		if is_prime(number):
			prime_counter += 1
	#print the prime when the counter = the goal
	if prime_counter == goal:
		print number

def is_prime(test):
	if test == 2:
		return True
	if test % 2 == 0:
		return False
	for d in xrange(3, int(math.sqrt(test)) + 1, 2):
		if test % d == 0:
			return False
	return True



