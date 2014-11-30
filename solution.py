def main(given_range):
	return square_of_sums(given_range) - sum_of_squares(given_range)

def square_of_sums(upper_bound):
	sums = 0
	for x in range(1, upper_bound + 1):
		sums += x
	return sums ** 2

def sum_of_squares(upper_bound):
	squares = 0
	for x in range(1, upper_bound + 1):
		squares += (x ** 2)
	return squares
