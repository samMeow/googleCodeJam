import sys
from itertools import repeat, chain
import math

if len(sys.argv) < 3:
	print("Usage `python3 base input_file output_file`")
	sys.exit(1)

def readFile(filename):
	data = []
	buffer_datum = {}
	next_line = False

	with open(filename) as f:
		line = f.readline()
		datum_line = 0
		for datum in f:
			if datum_line == 0:
				if buffer_datum: data.append(buffer_datum)
				[datum_line, size] = [int(x)for x in list(datum.split(' '))]
				next_line = True
				buffer_datum = {}
			elif next_line:
				buffer_datum['need'] = datum.strip('\n')
				buffer_datum['package'] = []
				next_line = False
			else:
				buffer_datum['package'].append(datum.strip('\n'))
				datum_line -= 1

		f.close()

	if buffer_datum: data.append(buffer_datum)

	return data

def check_valid_package(need, package):
	base = round(package / need)

	if package >= need * base * 0.9 and package <= need * base * 1.1:
		return True

	return False

def to_range(need, num):
	return [math.ceil(num / (need * 1.1)), math.floor(num/ (need * 0.9))]


def match_data(inte_list, acc_range):
	[a_min_r, a_max_r] = acc_range
	for datum in inte_list:
		[inte_min, inte_max] = datum
		if (inte_min <= a_max_r) and (inte_max >= a_min_r):
			return datum

	return None

def pick_package(packges_list, need, acc_range, exclude_row):

	temp_data = {}
	[min_r, max_r] = acc_range

	for idx, package in enumerate(packges_list):
		if exclude_row == idx:
			continue
		else:
			datum = match_data(package, acc_range)
			if(datum == None):
				return 0
			else:
				temp_data[idx] = datum

	for key, val in temp_data.items():
		packges_list[key].remove(val)


	return 1


def processDatum(datum):
	need = [int(x) for x in datum['need'].split(' ')]
	packages = [ [int(x) for x in package.split(' ')] for package in datum['package'] ]

	valid_packages = []
	for idx, ingredient in enumerate(packages):
		valid_packages.append([ inte for inte in ingredient if check_valid_package(need[idx], inte) ])


	valid_range = []
	for idx, valid_p in enumerate(valid_packages):
		tmp_range = [to_range(need[idx], inte) for inte in valid_p]
		tmp_range = sorted(tmp_range, key= lambda x: (x[0],x[1]))
		valid_range.append(tmp_range)


	min_package = min(valid_range, key=lambda x: len(x))

	min_idx = valid_range.index(min_package)

	total = 0
	for [min_range, max_range] in min_package:
		total += pick_package(valid_range, need, [min_range, max_range], min_idx)


	return total


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
