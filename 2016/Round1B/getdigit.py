import sys
from itertools import repeat, chain
from functools import reduce

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

def flatten(listOfLists):
    return list(chain.from_iterable(listOfLists))

def ocurrence_map(memo, val):
	if val in memo:
		memo[val] += 1
	else:
		memo[val] = 1
	return memo
def to_occurence_map(charlist):
	return reduce(ocurrence_map, flatten(charlist), {})

def subtract_map(a,b):
	for key in b:
		a[key] -= b[key]
		if(a[key] == 0): a.pop(key, None)
	return a

def extract_word(char_dict, num_map, times):
	return subtract_map(char_dict, {k: v* times for k,v in num_map.items()})

num_en = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
num_en_map = [to_occurence_map(x) for x in num_en]

def extract_from_dict(char_dict, char, num):

	final_num = []
	if char_dict.get(char):
		times = char_dict[char]
		extract_word(char_dict, num_en_map[num], times)
		final_num += list(repeat(num, times))
	return final_num

def processDatum(datum):
	char_list = list(datum)
	char_dict = to_occurence_map(char_list)

	final_num = []

	# 0Z, 2W,6X, 8G unique
	final_num += extract_from_dict(char_dict, 'Z' ,0)
	final_num += extract_from_dict(char_dict, 'W' ,2)
	final_num += extract_from_dict(char_dict, 'G' ,8)
	final_num += extract_from_dict(char_dict, 'X' ,6)

	#after 6, 7S unique
	final_num += extract_from_dict(char_dict, 'S' ,7)
	# #after 8, 3H unique
	final_num += extract_from_dict(char_dict, 'H' ,3)

	# #after 7V, 5V unique
	final_num += extract_from_dict(char_dict, 'V' ,5)

	# #after 5, 4F unique
	final_num += extract_from_dict(char_dict, 'F', 4)

	# #remain 1O, 9I
	final_num += extract_from_dict(char_dict, 'O', 1)
	final_num += extract_from_dict(char_dict, 'I', 9)

	final_num.sort()

	return "".join([str(x) for x in final_num])


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
