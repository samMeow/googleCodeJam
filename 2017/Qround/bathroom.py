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

def processDatum(datum):
	[bathroom, guy] = list(map(lambda x: int(x), datum.split(' ')))

	bin_case = math.ceil(math.log(guy+1 ,2))

	min_people = math.floor(bathroom / (2**bin_case)) -1

	if min_people < 0:
		return "0 0"

	tolerance_case = bathroom % (2**(bin_case))

	if(tolerance_case / (2**(bin_case-1)) >= 1):
		if (guy % (2**(bin_case-1)) <= (tolerance_case % (2**(bin_case-1)))):
			return "{0} {1}".format(min_people + 1, min_people+1)
		else:
			return "{0} {1}".format(min_people + 1, min_people)
	else:
		if (guy % (2**(bin_case-1)) <= (tolerance_case % (2**(bin_case-1)) ) ):
			return "{0} {1}".format(min_people +1, min_people)
		else:
			return "{0} {1}".format(min_people, min_people)


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
