import sys
from itertools import repeat, chain
import math

if len(sys.argv) < 3:
	print("Usage `python3 base input_file output_file`")
	sys.exit(1)

def readFile(filename):
	data = []
	with open(filename) as f:
		line = f.readline()
		for datum in f:
			data.append(datum.strip('\n'))
		f.close()
	return data

def flip_cake(pancake):
	return "-" if pancake == "+" else "+"

def flip_cake_list(pancake_list):
	return list(map(flip_cake, pancake_list))


def processDatum(datum):
	[pancake_str, size] = datum.split(' ')
	pancake_list = list(pancake_str)
	size = int(size)

	count = 0
	for i in range(len(pancake_str) - size+1):
		if pancake_list[i] == "-":
			pancake_list = pancake_list[0:i] + flip_cake_list(pancake_list[i: i+size]) + pancake_list[i+size:]
			count +=1

	if all(pancake == "+" for pancake in pancake_list):
		return count
	else:
		return "IMPOSSIBLE"


def outputFormat(case, result):
	return 'Case #{0}: {1}\n'.format(case + 1, result)

def writeFile(filename, data):
	fout = open(filename, "w")
	for idx, val in enumerate(data):
		fout.write(outputFormat(idx, val))
	fout.close()

def main():
	data = readFile(sys.argv[1]);
	writeFile(sys.argv[2], list(map(processDatum, data)))

if __name__ == "__main__":
	main();
