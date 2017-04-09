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
	pencil_list = list(datum)
	pencil_list = list(map(lambda x: int(x), pencil_list))

	buffer_list = list(reversed(pencil_list))

	for i in range(len(buffer_list)-1):
		if buffer_list[i] < buffer_list[i+1]:
			buffer_list = list(repeat(9,i +1))+ [ buffer_list[i+1] -1 ] + buffer_list[i+2:]

	buffer_list = list(reversed(buffer_list))
	buffer_list = list(map(lambda x:str(x), buffer_list))

	result = "".join(buffer_list).lstrip("0")

	return result


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
