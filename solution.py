import math, itertools


def main(desired_prime):
	return nth(desired_prime)


def nth(desired_prime):
	generator_title = prime_gen()
	for x in range(desired_prime - 1):
		next(generator_title)
	return next(generator_title)


def prime_gen():
	for x in itertools.count(2):
		if is_prime(x):	
			yield x
	

def is_prime(test):
	if test == 2:
		return True
	if test % 2 == 0:
		return False
	for d in xrange(3, int(math.sqrt(test)) + 1, 2):
		if test % d == 0:
			return False
	return True


def gen_test():
	for x in range(5):
		yield x
