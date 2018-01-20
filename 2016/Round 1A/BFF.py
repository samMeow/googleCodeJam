import sys
from itertools import repeat, chain
from functools import reduce
import copy

if len(sys.argv) < 3:
	print("Usage `python3 base input_file output_file`")
	sys.exit(1)

def readFile(filename):
	data = []
	with open(filename) as f:
		line = f.readline()
		datum_line = 0
		for datum in f:
			if datum_line == 0:
				datum_line = 1
			else:
				data.append(datum.strip('\n'))
				datum_line -= 1

		f.close()
	return data

def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))

def add_pair_to_dict(memo, val):
	[key1, key2] = val
	if key2 in memo:
		memo[key2].add(key1)
	else:
		memo[key2] = {key1}

	return memo


def list_to_graph_map(pair_list):
	return reduce( add_pair_to_dict, pair_list,{})

def longest_possible(BFF_list, key):
	long_list = [key]
	for i in range(len(BFF_list)):
		last_dig = long_list[-1]
		if(BFF_list[last_dig-1] not in long_list):
			long_list.append(BFF_list[last_dig-1])
	return long_list

def expand_reverse_possible(reversed_map, BFF_circle):
	last_dig = BFF_circle[-1]
	data = []

	for x in reversed_map.get(last_dig, []):
		if x not in BFF_circle:
			copy_circle = BFF_circle.copy()
			copy_circle.append(x)
			data.append(copy_circle)

	if len(data) == 0:
		data = [BFF_circle]

	return data

def processDatum(datum):
	BFF_list = [int(val) for val in datum.split(' ')]
	BFF_pair_list = [[idx+1, val] for idx,val in enumerate(BFF_list)];
	size = len(BFF_list)

	print("======================")
	BFF_long_list = [longest_possible(BFF_list, idx+1) for idx in range(size)]
	print(BFF_long_list)


	can_expand_BFF_long_list = [x for x in BFF_long_list if BFF_list[x[-1]-1] == x[-2]]

	reverse_BFF_map = list_to_graph_map(BFF_pair_list)


	print(can_expand_BFF_long_list)

	for i in range(size):
		can_expand_BFF_long_list = flatten([ expand_reverse_possible(reverse_BFF_map, val) for val in can_expand_BFF_long_list])


	circle_BFF_list = [x for x in BFF_long_list if BFF_list[x[-1]-1] == x[0]]

	max_len_data = max(can_expand_BFF_long_list + circle_BFF_list, key=lambda x:len(x))

	print(can_expand_BFF_long_list)
	print(circle_BFF_list)
	return "{0} {1}".format(max_len_data, len(max_len_data))


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
