import sys

def prepare_data():
    data = sys.stdin.readlines()
    temp = [ x.rstrip() for x in data[1:]]

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
        print("Case #{}: {}".format(idx + 1, "POSSIBLE"))

if __name__ == "__main__":
    main();