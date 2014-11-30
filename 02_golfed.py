n1 = n2 = 1
n3 = n1 + n2
sums = 0

while n3 <= 4000000:
	if not n3%2:
		sums = n3 + sums
	n1 = n2
	n2 = n3
	n3 = n1 + n2
print sums
