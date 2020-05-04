from sys import stdin

def readData():
    stdin.readline()
    line = stdin.readline()
    seq = [ int(x) for x in line.split(' ')]
    return seq

def gcd(A, B):
    x = A
    y = B
    if A < B:
        x = B
        y = A
    while y:
        x, y = y, x % y
    return x
    


def findInit(raw):
    for idx, x in enumerate(raw):
        if raw[idx + 1] != x:
            return idx

def solve(raw):
    init = findInit(raw)
    out = raw + [0]
    out[init+1] = gcd(raw[init], raw[init + 1])
    out[init] = int(raw[init] / out[init+1])
    for idx, x in enumerate(raw[init:]):
        out[init + idx + 1] = int(x / out[init + idx])
    for idx, x in enumerate(reversed(raw[:init])):
        out[init - idx - 1] = int(x / out[init - idx])
        
    used = sorted(list(set(out)))
    lookup = dict(zip(used, list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
    return ''.join([ lookup.get(x) for x in out ])

    
def main():
    time = int(stdin.readline())
    for idx in range(time):
        problem = readData()
        out = solve(problem)
        print("Case #{}: {}".format(idx + 1, out))

if __name__ == "__main__":
    main()