y = 0
for x in range(0, 1000):
	if not (x%3 and x%5):
		y = x + y
print y
