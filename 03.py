import math

n = 600851475143

factorlist = []
primeset = set()

def isprime(p):
	if p in primeset:
		return True
	if p % 2 == 0:
		return False
	for d in xrange(3, int(math.sqrt(p)) + 1, 2):
		if p % d == 0:
			return False
	primeset.add(p)
	return True

def factors(f):
	for d in xrange(2, int(math.sqrt(f)) + 1):
		if f % d == 0:
			if d not in factorlist:
				factorlist.append(d)
			if f / d not in factorlist:
				factorlist.append(f / d)
			factors(f / d)


factors(n)
factorlist.sort(reverse=True)

for q in factorlist:
	if isprime(q):
		print q
		break
