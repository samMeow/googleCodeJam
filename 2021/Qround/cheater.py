import sys
import math

def solution(sample):
    q_avg = [0 for x in range(10000)]
    u_avg = [0 for x in range(100)]
    for i in range(100):
        for j in range(10000):
            v = sample[i][j]
            if v:
                q_avg[j] += 100
                u_avg[i] += 1

    sus = [0 for x  in range(100)]
    for i in range(100):
        for j in range(10000):
            v = sample[i][j]
            u = u_avg[i] / 10000
            q = q_avg[j] / 10000

            skill = u / (1 - u)
            diff = q / (1-q)
            cost = math.log(skill) - math.log(diff)
            if v and cost < 0:
                sus[i] += -cost
            elif not v and cost > 0:
                sus[i] += cost
            
    return sus.index(max(sus))



testcase = sys.stdin.readline()
sys.stdin.readline()
for i in range(int(testcase)):
    buffer = []
    for _ in range(100):
        line = sys.stdin.readline().rstrip('\n')
        buffer.append([ x == '1' for x in list(line) ])
    ans = solution(buffer)
    print("Case #{}: {}".format(i+1, ans))
