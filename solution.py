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
#I guess I could save on a bit of computing power...
	if test == 2:
		return True
	if test == 3:
		return True
	if test == 5:
		return True
	if test == 7:
		return True
	if test == 11:
		return True
	if test == 13:
		return True
#...by eliminating some early divisors.
	if test % 2 == 0:
		return False
	if test % 3 == 0:
		return False
	if test % 5 == 0:
		return False
	if test % 7 == 0:
		return False
	if test % 11 == 0:
		return False
	if test % 13 == 0:
		return False
#maybe I should automate that idea...
#later, though; working code first.
	for d in xrange(3, int(math.sqrt(test)) + 1, 2):
		if test % d == 0:
			return False
	return True



