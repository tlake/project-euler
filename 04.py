digits = 1
n = 0
p = 0
answer = 0
pals = []

def firsthalf(x):
	fh = []
	fh.extend(str(x))
	if len(fh) % 2 != 0:
		return fh[:(len(fh) + 1) / 2]
	return fh[:len(fh)/2]

def secondhalfreversed(x):
	sh = []
	sh.extend(str(x))
	sh = sh[len(sh)/2:]
	return sh[::-1]

if digits > 0:
	for x in range(1, digits + 1):
		p = (p * 10) + 1
	n = 9 * p

for x in range(n, p - 1, -1):
	answer = x * n
	if firsthalf(answer) == secondhalfreversed(answer):
		pals.append(x * n)
	for y in range(n - 1, x - 1, -1):
		answer = y * x
		if firsthalf(answer) == secondhalfreversed(answer):
			pals.append(y * x)

pals.sort(reverse=True)
print pals[0]


#### Try to get from this functionality
#
#def firsthalf(x):
#	fh = []
#	fh.extend(str(x))
#	return fh[:len(fh)/2]
#
#### to this functionality
#
#def firsthalf(x):
#	fh = []
#	fh.extend(str(x))
#	if len(fh) % 2 != 0:
#		return fh[:(len(fh) + 1) / 2]
#	return fh[:len(fh)/2]
#
#### in only two symbols.
#
#
#
### TOTALLY DID, HERE'S HOW:
### [::-1]
