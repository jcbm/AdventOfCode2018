# https://adventofcode.com/2018/day/1

acc = 0
file = open("D:/input.txt", "r")
for line in file:
	current_number = int(line)
	# The sign of the numbers are preserved - addition of negative numbers equals subtraction
	acc +=current_number
print(acc)		