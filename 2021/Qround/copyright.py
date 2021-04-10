import sys
def negSolution(X, Y, seq):
    accu = 0
    lastStop = ''
    seq = list(seq)

    for i in range(len(seq) - 1):
        pair = ''.join(seq[i:i+2])
        if pair == 'CJ':
            accu += X
        if pair == 'JC':
            accu += Y
        if pair == 'CC' or pair == 'JJ':
            accu += 0
        if pair == 'C?':
            if X > 0:
                accu += 0
                seq[i+1] = 'C'
            else:
                accu += X
                seq[i+1] = 'J'
        if pair == 'J?':
            if Y > 0:
                accu += 0
                seq[i+1] = 'J'
            else:
                accu += Y
                seq[i+1] = 'C'
        if pair == '?C':
            if lastStop == 'J':
                accu += Y
        if pair == '?J':
            accu += 0
            if lastStop == 'C':
                accu += X
        if pair == '??':
            accu += 0
    return accu


def solution(X, Y, seq):
    accu = 0
    seq = list(seq)
    for i in range(len(seq) - 1):
        pair = ''.join(seq[i:i+2])
        if pair == 'CJ':
            accu += X
        if pair == 'JC':
            accu += Y
        if pair == 'CC' or pair == 'JJ':
            accu += 0
        if pair == 'C?':
            accu += 0
            seq[i+1] = 'C'
        if pair == 'J?':
            accu += 0
            seq[i+1] = 'J'
    return accu



testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line1 = sys.stdin.readline().rstrip('\n')
    X, Y, seq = line1.split(' ')
    if int(X) < 0 or int(Y) < 0:
        ans = negSolution(int(X), int(Y), seq)
    else:
        ans = solution(int(X), int(Y), seq)
    print("Case #{}: {}".format(i+1, ans))
