import sys
from math import gcd
# from fractions import Fraction
class Fraction:
    def __init__(self, a, b):
        common = gcd(a, b)
        self.top = a // common
        self.bottom = b // common

    def __eq__(self, other):
        return self.top == other.top and self.bottom == other.bottom

    def __ge__(self, other):
        return (self.top / self.bottom) >= other

    def __le__(self, other):
        return (self.top / self.bottom) <= other

    def __hash__(self):
        return self.__str__().__hash__()

    def __str__(self):
        return 'Fraction({}, {})'.format(self.top, self.bottom)


def sum_floor(ar, determiner):
    return sum([ x // determiner for x in ar ])

def solution(n, d, dinner):

    # e.g 4 5 [1, 10, 9, 1000] then 1st round [1000 /2] = 500
    # floor(1 / 500) + floor(10/500) + floor(9/500) + floor(1000/500) = 2 < 5 then we pick 250 for next
    l = 0
    r = 1e25
    c = (l + r) / 2
    for _ in range(0, 300):
        c = (l+ r) /2
        if sum_floor(dinner, c) >= d:
            l = c
        else:
            r = c
    
    dinner = sorted(dinner)
    choice = {}
    for cake in dinner:
        for i in range(1, d + 1):
            target = Fraction(cake, i)
            if target <= c:
                [common, final] = choice.get(target, (0, 0))
                if final + i <= d:
                    choice[target] = (common + 1, final + i)

    print(choice)
    max_common = 1
    for _, v in choice.items():
        [common, _] = v
        if common > max_common:
            max_common = common

    return d - max_common

line = sys.stdin.readline()
testcase = int(line.rstrip('\n'))
for i in range(testcase):
    [n, d] = sys.stdin.readline().rstrip('\n').split()
    dinner = sys.stdin.readline().rstrip('\n').split()
    print("Case #{}: {}".format(i+1, solution(
        int(n),
        int(d),
        [ int(d) for d in dinner ],
    )))