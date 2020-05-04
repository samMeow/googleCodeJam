import sys

def flip(ar):
    buffer = []
    for a in ar:
        if a == '0':
            buffer.append('1')
        elif b == '1':
            buffer.append('0')
        else:
            buffer.append('')
    return buffer

def interactive(b):
    buffer = [ '' for _ in range(b) ]
    print('0')
    bit = sys.stdin.readline()
    while bit != 'N' or bit != 'Y':
        for _ in range(5):
            idx = buffer.find('')
            print(idx)
            bit = sys.stdin.readline()
            buffer[idx] = bit.rstrip('\n')
        for _ in range(5):
            idx = buffer.rfind('')
            print(idx)
            bit = sys.stdin.readline()
            buffer[idx] = bit.rstrip('\n')
            
        

line = sys.stdin.readline()
testcase, b = [ int(x) for x in line.rstrip('\n').split(' ') ]
for i in range(testcase):
