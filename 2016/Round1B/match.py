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


def A_larger_B_case(curr_A, currB):
	if curr_A == '?' and curr_B == '?':
		sug_A = 0
		sug_B = 9
	elif curr_A == '?':
		sug_A = 0
		sug_B = int(curr_B)
	elif curr_B == '?':
		sug_A = int(curr_A)
		sug_B = 9
	else:
		sug_A = int(curr_A)
		sug_B = int(curr_B)

	return [sug_A, sug_B]

def min_equal_case(curr_A, curr_B):
	if curr_A == '?' and curr_B == '?':
		sug_A = 0
		sug_B = 0
	elif curr_A == '?':
		sug_A = int(curr_B)
		sug_B = int(curr_B)
	elif curr_B == '?':
		sug_A = int(curr_A)
		sug_B = int(curr_A)
	else:
		sug_A = int(curr_A)
		sug_B = int(curr_B)

	return [sug_A, sug_B]

def not_equal_case(last_suggest, last_real,current_real):
	[last_sA, last_sB] = last_suggest
	[curr_A, curr_B] = current_real

	if curr_A != '?' and curr_B != '?':
		[sug_lA, sug_lB] = last_suggest

	return last_suggest



def suggest_digit(last_suggest, last_real, current_real):
	[last_sA, last_sB] = last_suggest
	[last_A, last_B] = last_real
	[curr_A, curr_B] = current_real


	if last_sA != last_sB:
		[sug_lA, suglB] = last_suggest
		if last_sA > last_sB:
			[sug_A, sug_B] = A_larger_B_case(curr_A, curr_B)
		else:
			[sug_B, sug_A] = A_larger_B_case(curr_B, curr_A)
	else:
		if last_real != '?' and last_real != '?':
			[sug_lA, suglB] = last_suggest
			[sug_A, sug_B] = min_equal_case(curr_A, curr_B)
		else:

	return [sug_lA, suglB, sug_A, sug_B]


def processDatum(datum):
	[A_score, B_score] = list(map(lambda x: list(x), datum.split(" ")))

	suggest_A = [0] * len(A_score)
	suggest_B = [0] * len(A_score)
	for i in range(len(A_score)):
		if i == 0:
			[suggest_A[0], suggest_B[0]] = min_equal_case(A_score[0], B_score[0])
		else:
			[suggest_A[i], suggest_B[i]] = min_equal_case(A_score[i], B_score[i])


	print(suggest_A, suggest_B)

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
