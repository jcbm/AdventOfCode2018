# https://adventofcode.com/2018/day/1

import itertools

def read_input_file():
	file = open("data/Day01-input.txt", "r")
	return map(int, file)

def part1():
	numbers = read_input_file()	
	acc = 0
	for current_number in numbers:		
		# The sign of the numbers are preserved - addition of negative numbers equals subtraction
		acc +=current_number
	return acc

def part2():
	numbers = read_input_file()
	seen_values = set()
	acc = 0
	generator = itertools.cycle(numbers)
	for current_number in generator:
		acc += current_number
		if (acc in seen_values):
			return acc 
		else: 
			seen_values.add(acc)
		
if __name__ == "__main__":
	print("Solution to part 1: " + str(part1()))
	print("Solution to part 2: " + str(part2()))
	