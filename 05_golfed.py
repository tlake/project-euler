import math

def is_prime(x):
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for y in xrange(3, int(math.sqrt(x)) + 1, 2):
		if x % y == 0:
			return False
	return True

def power_trip(n, user_input):
	expo = 1
	while n ** (expo + 1) <= user_input:
		expo += 1
	return n ** expo

def main(user_input):
	running_product = 1
	for i in xrange(2, user_input + 1):
		if is_prime(i):
			running_product *= power_trip(i, user_input)
	return running_product
