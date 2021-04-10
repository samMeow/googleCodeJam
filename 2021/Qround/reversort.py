import sys

def solution(N, C):
    if C < N-1:
        return 'IMPOSSIBLE'
    if C > N * (N+1) /2 - 1:
        return 'IMPOSSIBLE'
    
    target = C - N + 1
    temp = list(range(N))
    for i in range(N):
        if target >= N - 1 - i:
            temp[i:] = list(reversed(temp[i:]))
            target -= N - 1 - i
        else:
            temp[i:i+target+1] = list(reversed(temp[i:i+target+1]))
            break

    buffer = list(range(N))
    for i, v in enumerate(temp):
        buffer[v] = str(i + 1)
    return ' '.join(buffer)


testcase = sys.stdin.readline()
for i in range(int(testcase)):
    N, C = sys.stdin.readline().rstrip('\n').split(' ')
    ans = solution(int(N), int(C))
    print("Case #{}: {}".format(i+1, ans))
