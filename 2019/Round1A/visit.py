import sys

def prepare_data():
    data = sys.stdin.readlines()
    temp = [ x.rstrip().split(' ') for x in data[1:]]
    return [  [ int(x) for x in ar ]  for ar in temp ]

def cantJump(src, dest, visits):
    if src[0] == dest[0]:
        return True
    if src[1] == dest[1]:
        return True
    if (src[0] + src[1]) == (dest[0] + dest[1]):
        return True
    if (src[0] - src[1]) == (dest[0] - dest[1]):
        return True
    
    if visits[dest[0]][dest[1]]:
        return True

    return False

def distance(A, B):
    return (A[0] - B[0]) ^ 2 + (A[1] - B[1]) ^ 2

def minByDis(src, poss):
    min = 99999
    lastPt = src 
    for pt in poss:
        if distance(src, pt) < min:
            min = distance(src, pt)
            lastPt = pt
    return lastPt


def get_next(curPt, R, C, visits):
    possible = []
    for i in range(R):
        for j in range(C):
            if cantJump(curPt, [i, j], visits) == False:
                possible.append([i ,j])
    if possible:
        return minByDis(curPt, possible)
    return False

def solve(R, C):
    visits = [ [False for j in range(C)] for i in range(R) ]
    startPt = [0, 0]
    route = [startPt]
    visits[0][0] = True

    curPt = startPt
    for _ in range(R *C - 1):
        nextPt = get_next(curPt, R, C, visits)
        if nextPt:
            curPt = nextPt
            route.append(nextPt)
            visits[nextPt[0]][nextPt[1]] = True
            continue
        return []

    return [ [pt[0] + 1, pt[1] + 1] for pt in route ]
    
    
def main():
    data = prepare_data()
    for idx, problem in enumerate(data):
        [x, y] = problem
        can = solve(x, y)
        if can:
            print("Case #{}: {}".format(idx + 1, "POSSIBLE"))
            for pt in can:
                print("{} {}".format(pt[0], pt[1]))
        else:
            print("Case #{}: {}".format(idx + 1, "IMPOSSIBLE"))

if __name__ == "__main__":
    main();