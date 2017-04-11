import sys
from itertools import repeat, chain
from functools import reduce

if len(sys.argv) < 3:
	print("Usage `python3 base input_file output_file`")
	sys.exit(1)

def readFile(filename):
	data = []
	buffer_datum = []
	with open(filename) as f:
		line = f.readline()
		datum_line = 0
		for datum in f:
			if datum_line == 0:
				if buffer_datum: data.append(buffer_datum)
				datum_line = int(datum) * 2 -1
				buffer_datum = []
			else:
				buffer_datum.append(datum.strip('\n'))
				datum_line -= 1

		f.close()

	if buffer_datum: data.append(buffer_datum)

	return data

def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))

def to_int_list(some_list):
	return list(map(lambda x: int(x), some_list))

def ocurrence_map(memo, val):
	if val in memo:
		memo[val] += 1
	else:
		memo[val] = 1
	return memo

def processDatum(datum):
	solider_list = list(map(lambda x: to_int_list(x.split(' ')), datum))


	# sorted list
	solider_map = reduce(ocurrence_map, flatten(solider_list), {})

	remain = [ k for k,v in solider_map.items() if v%2 == 1];

	remain.sort()


	return " ".join([ str(v) for v in remain])


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
