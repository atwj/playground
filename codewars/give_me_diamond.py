"""
Give Me Diamond question from codewars
"""
def diamond(n):
# Make some diamonds!
	if n % 2 == 0: return None
	if n == 1: return '*'

	output = ''
	spaces = int(n / 2)
	counter = 1

	output += (' ' * spaces) + '*\n'
	star_count = counter
	while counter < n:
		if (counter + 2) <= n:
			spaces -= 1
			star_count += 2
			output += (' ' * spaces) + ('*' * star_count) + '\n'
		else:
			spaces += 1
			star_count -= 2
			output += (' ' * spaces) + ('*' * star_count) + '\n'

		counter += 1
	return output

print(diamond(3))