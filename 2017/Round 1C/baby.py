import sys
from itertools import repeat
from functools import reduce
import math

if len(sys.argv) < 3:
	print("Usage `python3 base input_file output_file`")
	sys.exit(1)

def readFile(filename):
	data = []
	ac_datum = []
	aj_datum = []

	with open(filename) as f:
		line = f.readline()
		ac_datum_line = 0
		aj_datum_line = 0
		need = 0
		for datum in f:
			if ac_datum_line == 0 and aj_datum_line == 0:
				if ac_datum or aj_datum: data.append([ac_datum, aj_datum])
				[ac_datum_line, aj_datum_line] = [int(x)for x in list(datum.split(' '))]
				ac_datum = []
				aj_datum = []
			elif ac_datum_line != 0:
				ac_datum.append(datum.strip('\n'))
				ac_datum_line -= 1
			else:
				aj_datum.append(datum.strip('\n'))
				aj_datum_line -= 1

		if ac_datum or aj_datum: data.append([ac_datum, aj_datum])
		f.close()
	return data



def processDatum(datum):

	[ac, aj] = datum

	ac_time = [ [int(x) for x in time.split(' ')]for time in ac]
	aj_time = [ [int(x) for x in time.split(' ')]for time in aj]

	ac_time = sorted(ac_time, key=lambda x: x[0])
	aj_time = sorted(aj_time, key=lambda x: x[0])

	ac_remain = 720 - sum([ time[1] - time[0] for  time in aj_time])
	aj_remain = 720 - sum([ time[1] - time[0] for  time in ac_time])

	print(ac_remain, aj_remain)


	merge_time = [ ['j', time] for time in ac_time ] +  [ ['c', time] for time in aj_time ]
	merge_time = sorted(merge_time, key=lambda x: x[1])

	print(merge_time)

	return datum


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
