import sys
import heapq

def solution(data, pos):
    lookup = {}
    for i, v in enumerate(pos):
        lookup[v-1] = lookup.get(v-1, [])
        lookup[v-1].append(i)
    
    heaplookup = {}
    stack = [-1]
    while len(stack) > 0:
        last = stack.pop()
        if lookup.get(last):
            if heaplookup.get(lookup[last][0]):
                heaplookup[last] = list(heapq.merge(
                    *[ heaplookup[x] for x in lookup[last] ]
                ))
                if last == -1:
                    continue
                if data[last] > heaplookup[last][0]:
                    heapq.heappushpop(heaplookup[last], data[last])
            else:
                stack.append(last)
                for v in lookup[last]:
                    stack.append(v)
        else:
            heaplookup[last] = []
            heapq.heappush(heaplookup[last], data[last])

    return sum(heaplookup.get(-1, []))

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    sys.stdin.readline()
    line1 = sys.stdin.readline().rstrip('\n')
    line2 = sys.stdin.readline().rstrip('\n')
    ans = solution(
        [ int(x) for x in line1.split(' ') ],
        [ int(x) for x in line2.split(' ') ],
    )
    print("Case #{}: {}".format(i+1, ans))
