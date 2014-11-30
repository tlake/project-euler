import math

top = 20

def is_prime(x):
	if x == 2:
		return True
	if x % 2 == 0:
		return False
	for y in xrange(3, int(math.sqrt(x)) + 1, 2):
		if x % y == 0:
			return False
	return True

def power_trip(x):
	if x * x > top:
		return x
	y = 2
	while x ** y <= top:
		y += 1
	return (x ** (y - 1))

def main(x):
	n = 1
	for y in xrange(2, x + 1):
		if is_prime(y):
			n = n * power_trip(y)
	return n

print main(top)
