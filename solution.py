import pprint
def firsthalf(x):
	fh = []
	fh.extend(str(x))
	return fh[:len(fh)/2]

def secondhalfreversed(x):
	sh = []
	sh.extend(str(x))
	sh = sh[len(sh)/2:]
	return sh[::-1]


#find number of digits
digits = 3
n = 0
p = 0
answer = 0


#generate the largest number to be multiplied
if digits > 0:
	for x in range(1, digits + 1):
		p = (p * 10) + 1
n = 9 * p

#begin multiplying downward:
#	for each na, do (na * nb),
#	where nb decreases by 1 from n to na.
pals = []
for x in range(n, p, -1):
	answer = x * n
#	print x, " x ", n, " = ", x * n
	if firsthalf(answer) == secondhalfreversed(answer):
		print x, "x", n, "=", x * n#, " PALINDROME"
#		string = str(x * n) + "=" + str(x) + "x" + str(n) 
#		pals.append(string)
		pals.append(x * n)
		break
	for y in range(n, x - 1, -1):
		answer = y * x
#		print y, " x ", x, " = ", y * x
		if firsthalf(answer) == secondhalfreversed(answer):
			print y, "x", x, "=", y * x#, " PALINDROME"
#			string = str(y * x) + "=" + str(y) + "x" + str(x)
#			pals.append(string)
			pals.append(y * x)
			break
pals.sort(reverse=True)
pprint.pprint(pals)


