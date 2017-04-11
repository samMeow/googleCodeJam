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

def processDatum(datum):
	word_list = list(datum)

	output = []

	for char in word_list:
		if not output:
			output = [char]
		else:
			if output[0] > char:
				output.append(char)
			else:
				output.insert(0, char)

	return "".join(output)

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
