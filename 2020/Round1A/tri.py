import sys
import math

facdict = {
    0: 1,
    1: 1
}
def fac(n):
    if n < 0:
        return 1
    if facdict.get(n, None):
        return facdict[n]
    facdict[n] = n * fac(n -1)
    return facdict[n]

def nCr(n, r): 
    return fac(n) // (fac(n-r) * fac(r))

def validVisit(node, visited):
    (r, k) = node
    if r < 1 or k < 1:
        return False
    if r > 500:
        return False
    if k >= 2 * r:
        return False
    if node in visited:
        return False
    return True


def largeSolution(target):
    bin = "{0:b}".format(target-30)
    stack = []
    left = False

    stack = []
    left = True
    rev = [*reversed(bin)]
    oneCount = 0
    # 2^30 > 10^9
    for i in range(30):
        if i >= len(rev) or rev[i] == '0':
            if left:
                stack.append((i+1, 1))
            else:
                stack.append((i+1, i+1))
        elif rev[i] == '1':
            oneCount = oneCount + 1
            if left:
                for n in range(i+1):
                    stack.append((i+1, n+1))
                left = False
            else:
                for n in reversed(range(i + 1)):
                    stack.append((i+1, n+1))
                left = True

    for i in range(30, 30 + oneCount):
        if left:
            stack.append((i+1, 1))
        else:
            stack.append((i+1, i+1))
    
    return stack


def smallSolution(target):
    return [(n+1, 1) for n in range(target)]
    

def solution(target):
    if target > 400:
        return largeSolution(target)
    else:
        return smallSolution(target)
    # stacks = [[(1,1),[(1, 1)]]]
    # while len(stacks) != 0:
    #     [(r, k), visited] = stacks.pop(0)
    #     total = sum([  nCr(n-1, r-1) for (n, r) in visited ])
    #     if total > target:
    #         continue
    #     if total == target:
    #         return visited
    #     newVisits = [
    #         (r, k - 1),
    #         (r, k + 1),
    #         (r + 1, k),
    #         (r + 1, k + 1),
    #         (r - 1, k - 1),
    #         (r - 1, k),
    #     ]
    #     valid = [n for n in newVisits if validVisit(n, visited)]
    #     for node in valid:
    #         path = visited[:]
    #         path.append(node)
    #         stacks.append([node, path])
    # return False


line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    line = sys.stdin.readline()
    print("Case #{}: \n{}".format(
        i + 1,
        '\n'.join([ '{} {}'.format(k, r) for (k, r) in solution(int(line))])
    ))
    
    