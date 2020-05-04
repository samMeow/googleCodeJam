import sys


def solution(u, buffer):
    cases = sorted(buffer, key=lambda tup: tup[0])
    my_dict = {}
    for line in cases:
        [query, res] = line
        for token in res:
            if query == -1:
                query = 10 ** u -1
            if not my_dict.get(token):
                my_dict[token] = 10
            if len(str(query)) == len(res):
                if my_dict[res[0]] > int(str(query)[0]):
                    my_dict[res[0]] = int(str(query)[0])
    buffer = sorted(my_dict.items(), key = lambda tup: tup[1])

    return ''.join([ k for (k,v) in ([buffer[-1]] + buffer[0:9]) ])

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    u = int(sys.stdin.readline())
    buffer = []
    for _ in range(10 ** 4):
        [query, res] = sys.stdin.readline().rstrip('\n').split()
        buffer.append([int(query), res])

    print("Case #{}: {}".format(i+1, solution(
        u,
        buffer
    )))