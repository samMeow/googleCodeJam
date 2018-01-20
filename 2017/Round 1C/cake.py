import sys
from itertools import repeat
from functools import reduce
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
		need = 0
		for datum in f:
			if datum_line == 0:
				if buffer_datum: data.append([need, buffer_datum])
				[datum_line, need] = [int(x)for x in list(datum.split(' '))]
				buffer_datum = []
			else:
				buffer_datum.append(datum.strip('\n'))
				datum_line -= 1

		if buffer_datum: data.append([need, buffer_datum])
		f.close()
	return data


def total_area(cake):
	[rad, height] = cake
	return math.pi * rad * rad + 2 * math.pi * rad * height

def round_area(cake):
	[rad, height] = cake
	return 2 * math.pi * rad * height

def add_radius_area(cake, radius):
	[rad, height] = cake
	return round_area(cake) + (rad * rad - radius * radius) * math.pi


def update_relative_list(cake, radius):
	if cake[0] > radius:
		return [cake[0], cake[1], add_radius_area(cake[0:2], radius)]
	else:
		return [cake[0], cake[1], round_area(cake[0:2])]

def processDatum(datum):
	[need, cakes] = datum

	cakes = [ [int(x) for x in list(cake.split(' '))] for cake in cakes]

	relative_list = [ [cake[0], cake[1], total_area(cake)] for cake in cakes]
	area = 0
	base_radius = 0

	while need > 0:
		need_cake = max(relative_list, key=lambda x: x[2])
		[rad, height, relative_area] = need_cake
		relative_list.remove(need_cake)

		if rad > base_radius: base_radius = rad;
		area += relative_area

		relative_list = [  update_relative_list(cake, base_radius)  for cake in relative_list]
		need -= 1

	return area

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
