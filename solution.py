top = 10


def find_max(a):
	b = 1
	for c in range((a / 2) + 1, a + 1):
		b = c * b
	return b


def divides_evenly(test):
	for x in range ((top / 2) + 1, top + 1):
		if test % x != 0:
			return False
	return True


for t in xrange(top ** 2, find_max(top), top):
	if divides_evenly(t):
		print t
		break
