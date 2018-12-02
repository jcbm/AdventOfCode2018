# https://adventofcode.com/2018/day/2

from collections import Counter 

def read_input_file():
	#file= open("data/Day02-testdata.txt", "r")
	file = open("data/Day02-input.txt", "r")
	return file.readlines()

def part1():
	labels = read_input_file()
	two_count = 0
	three_count = 0
	for line in labels: 
		counter = Counter(line)
		if 2 in counter.values():
			two_count += 1
		if 3 in counter.values():
			three_count += 1
	return two_count * three_count
	

def part2():
	labels = read_input_file()
	for label1 in labels:
		for label2 in labels:
			differences=[i for i in range(len(label1)) if label1[i] != label2[i]]
			if (len(differences) == 1):
				differing_char_index = differences[0]
				return label1[:differing_char_index] + label1[differing_char_index+1:]
				
				
if __name__ == "__main__":
	print("Solution to part 1: " + str(part1()))
	print("Solution to part 2: " + part2())
	