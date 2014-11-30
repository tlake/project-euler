import math

n = 600851475143

def isprime(p):
	if p == 2:
		return True
	if p % 2 == 0:
		return False
	for d in xrange(3, int(math.sqrt(p)) + 1, 2):
		if p % d == 0:
			return False
	return True

def factors(f):
	factorlist = []
	for d in xrange(2, int(math.sqrt(f)) + 1):
		if f % d == 0:
			if d not in factorlist:
				factorlist.append(d)
			if f / d not in factorlist:
				factorlist.append(f / d)
			factorlist.extend(factors(f / d))
			break
	factorlist.sort(reverse=True)	
	return factorlist

for q in factors(n):
	if isprime(q):
		print q
		break
