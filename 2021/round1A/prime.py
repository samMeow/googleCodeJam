import sys

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499]

def prime_factor(n):
    temp = n
    result = {}
    for d in primes:
        while temp % d == 0:
            result[d] = result.get(d, 0) + 1
            temp = temp / d
    if temp > 1:
        return None
    return result

def is_sub(a, b):
    for i, v in b.items():
        if a.get(i, 0) < v:
            return False
    return True

def add_set(a, b):
    result = { **a }
    for i, v in b.items():
        result[i] = result.get(i, 0) + v
    return result
def subtract_set(a, b):
    result = {**a}
    for i, v in b.items():
        result[i] = result.get(i, 0) - v
        if result[i] == 0:
            del result[i]
    return result

def is_equal(a, b):
    result = { **a }
    for i, v in b.items():
        result[i] = result.get(i, 0) - v
    return not any(result.values())

def sum_map(map):
    sum = 0
    for i, v in map.items():
        sum += i * v
    return sum

def solution(map):
    total = sum_map(map)

    for x in range(total-1, 1, -1):
        diff_map = prime_factor(x)
        if not diff_map:
            continue
        if not is_sub(map, diff_map):
            continue
        remain = subtract_set(map, diff_map)
        if sum_map(remain) == x:
            return x
        
    return 0

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    sets = sys.stdin.readline()
    buffer = {}
    for _ in range(int(sets)):
        line2 = sys.stdin.readline().rstrip('\n')
        ques = [ int(x) for x in line2.split(' ') ]
        buffer[ques[0]] = ques[1]
    print("Case #{}: {}".format(i+1, solution(buffer)))