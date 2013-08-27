import math, itertools


def nth_prime(goal):
	return list(itertools.islice((x for x in itertools.count(1) if is_prime(x)), goal - 1, goal))



def is_prime(test):
	if test == 2:
		return True
	if test % 2 == 0:
		return False
	for d in xrange(3, int(math.sqrt(test)) + 1, 2):
		if test % d == 0:
			return False
	return True



