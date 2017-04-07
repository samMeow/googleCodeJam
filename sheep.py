import sys
from itertools import repeat

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

def tokenizeNum(num):
	return list(map(lambda x: int(x),list(str(num))))

def processDatum(datum):
	num_from_datum = int(datum)
	if num_from_datum == 0: return "IMPOSSIBLE"

	current_num = num_from_datum
	num_ar = list(repeat(False, 10))

	for num in tokenizeNum(current_num):
		num_ar[num] = True

	while(all(num == True for num in num_ar) != True):
		current_num += num_from_datum
		for num in tokenizeNum(current_num):
			num_ar[num] = True

	return current_num

def outputFormat(case, result):
	return 'Case #{0}: {1}\n'.format(case, result)

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
