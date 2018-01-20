import sys
from itertools import repeat, chain
import math

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
				[datum_line, size] = [int(x)for x in list(datum.split(' '))]
				buffer_datum = []
			else:
				buffer_datum.append(datum.strip('\n'))
				datum_line -= 1

		f.close()

	if buffer_datum: data.append(buffer_datum)

	return data



def fill_row(cake_list, point):
	[x, y] = point
	letter = cake_list[y][x]

	left_most = x
	right_most = x +1

	# fill left
	for i in reversed(range(x)):
		if cake_list[y][i] != '?':
			break;
		else:
			left_most = i
			cake_list[y][i] = letter

	#fill right
	for i in range( x+1 ,len(cake_list[y])):
		if cake_list[y][i] != '?':
			break;
		else:
			right_most = i + 1
			cake_list[y][i] = letter

	return [left_most, right_most]


def block_fill_col(cake_list, sample_row, sample_row_size):
	[lm, rm] = sample_row_size
	letter = cake_list[sample_row][lm]

	# fill top
	for j in reversed(range(sample_row)):
		if all([char == '?' for char in cake_list[j][lm:rm]  ]):
			cake_list[j][lm:rm] = list( repeat(letter, len(cake_list[j][lm:rm])) )
		else:
			break;

	#fill bottom
	for j in range(sample_row+1, len(cake_list)):
		if all([char == '?' for char in cake_list[j][lm:rm]]):
			cake_list[j][lm:rm] = list( repeat(letter, len(cake_list[j][lm:rm])) )
		else:
			break;

	return;

def processDatum(datum):
	cake_list = [list(row) for row in datum]
	col_size = len(cake_list)
	row_size = len(cake_list[0])

	have_letter_cord = []

	for y in range(col_size):
		for x in range(row_size):
			if cake_list[y][x] != '?':
				have_letter_cord.append([x, y])

	for [x,y] in have_letter_cord:
		[lm, rm] = fill_row(cake_list, [x,y])
		block_fill_col(cake_list, y, [lm, rm])

	cake_list = [ "".join(row) for row in cake_list]
	return "\n"+"\n".join(cake_list)

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
