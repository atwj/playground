"""
Give Me Diamond question from codewars
"""
def diamond(n):
	# Make some diamonds!
	if not n: return None
	if n % 2 == 0: return None
	if n == 1: return '*'
	output = ''
	no_of_spaces = int(n / 2)
	space = ' '
	
	counter = 0
	while counter < n:
		if (counter * 2 + 1) <= n:
			output += (space * no_of_spaces) + ('*' * (n -  (2 *no_of_spaces))) + '\n'
			if no_of_spaces > 0: no_of_spaces -= 1 
		else:
			no_of_spaces += 1
			output += (space * no_of_spaces) + ('*' * (n -  (2 *no_of_spaces))) + '\n'
		counter += 1
	return output

print(diamond(''))