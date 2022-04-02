import sys

def small_possible(a, b):
    strb = str(b)
    stra = str(a)
    if b > int(stra[0:len(strb)]):
        return int(strb.ljust(len(stra), '0')), len(stra) - len(strb)

    if b < int(stra[0:len(strb)]):
        return int(strb.ljust(len(stra) + 1, '0')), len(stra) - len(strb) + 1

    if a == b:
        return int(strb.ljust(len(stra) + 1, '0')), len(stra) - len(strb) + 1
    
    if stra[len(strb):] == '9' * (len(stra) - len(strb)):
        return int(strb.ljust(len(stra) + 1, '0')), len(stra) - len(strb) + 1
    
    return a + 1, len(stra) - len(strb)  

def solution(numbers):
    last_min = -1
    digit = 0
    for n in numbers:
        if n > last_min:
            last_min = n
            continue
        temp, added = small_possible(last_min, n)
        last_min = temp
        digit += added
    return digit

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline().rstrip('\n')
    ques = [ int(x) for x in line2.split(' ') ]
    print("Case #{}: {}".format(i+1, solution(ques)))
