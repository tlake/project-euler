import math, itertools


def nth(desired_prime, iterable):
	the_generator = iterable
	for x in range(desired_prime - 1):
		next(the_generator)
	return next(the_generator)

def prime_gen():
	return (x for x in itertools.count(2) if is_prime(x))	

	# This is just sugar for
	#	for x in itertools.count(2):
	#		if is_prime(x):	
	#			yield x
	# The round brackets make a generator,
	# square brackets would make a list.
	# A list here would be bad. It would be infinitely big.
	# Lol.
	

def is_prime(test):
	if test == 2:
		return True
	if test % 2 == 0:
		return False
	for d in xrange(3, int(math.sqrt(test)) + 1, 2):
		if test % d == 0:
			return False
	return True


def nth_prime(desired_prime):
	generator_title = prime_gen()
	for x in range(desired_prime - 1):
		next(generator_title)
	return next(generator_title)
