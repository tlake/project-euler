y = 0
for x in range(0, 1000):
	if (x/3) - (x/3.0) == 0.0:
		y = x + y
	elif (x/5) - (x/5.0) == 0.0:
		y = x + y
print y
