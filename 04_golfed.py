digits = 5
biggest = 10 ** digits - 1
lower_bound = (biggest / 9) * 8
pals = set()


def ispalindrome(given_product):
	return str(given_product) == str(given_product)[::-1]

assert digits != 0, "Need some positive digits, yo."

assert digits > 0, "The fuck do you hope to accomplish with negative digits?"

for primary_count in range(biggest, lower_bound - 1, -1):
	for secondary_count in range(biggest, primary_count - 1, -1):
		product = secondary_count * primary_count
		if ispalindrome(product):
			pals.add(product)

print max(pals)
