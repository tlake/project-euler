import math, itertools


def nth(desired_prime, iterable):
	the_generator = iterable
	for x in range(desired_prime - 1):
		next(the_generator)
	return next(the_generator)


def prime_gen():
	return (x for x in itertools.count(2) if is_prime(x))


def is_prime(test):
	if test == 2:
		return True
	if test % 2 == 0:
		return False
	for d in xrange(3, int(math.sqrt(test)) + 1, 2):
		if test % d == 0:
			return False
	return True
