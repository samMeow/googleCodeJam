import sys

min_roar = {
    2: 12,
    3: 123,
    4: 1011,
    5: 12345,
    6: 100101,
    7: 1234567,
    8: 10001001,
    9: 100101102,
    10: 1000010001,
    11: 12345678910,
    12: 100000100001,
    13: 1234567891011,
    14: 10000001000001,
    15: 100001000110002,
    16: 1000000010000001,
    17: 12345678910111213,
    18: 100000000100000001,
}

# test case = 18 digit (so at most group 10 digit)
def solution(year):
    intyear = int(year)
    if intyear < 12:
        return '12'
    digits = len(year)
    consider_size = min(int(digits / 2) + 1, 11)
    consider = []
    # e.g. 7899
    for i in range(1, consider_size):
        first_number = int(year[:i])
        buffer = [str(first_number)]
        temp = first_number
        while len(''.join(buffer)) < size:
            temp = temp + 1
            buffer.append(str(temp))


    # consider = []
    # 
    # for i in range(1, consider_size):
    #     first_number = int(year[:i])
    #     buffer = [str(first_number)]
    #     temp = first_number
    #     while len(''.join(buffer)) < size:
    #         temp = temp + 1
    #         buffer.append(str(temp))
        
        # if int(''.join(buffer)) > intyear:
        #     consider.append(''.join(buffer))
    #     # also add next
    #     first_size = i
    #     buffer2 = [ str(int(x) + 1) for x in buffer]
    #     while len(buffer2[0]) == i:
    #         while len(''.join(buffer2)) > size:
    #             buffer2.pop()
    #         if len(buffer2) == 0:
    #             break
    #         if int(''.join(buffer2)) > intyear:
    #             consider.append(''.join(buffer2))
    #             break
    #         buffer2 = [ str(int(x) + 1) for x in buffer2]
    #     if int(''.join(buffer2)) > intyear:
    #         consider.append(''.join(buffer2))

    # consider = [ int(x) for x in consider]
    # return min(consider)

testcase = sys.stdin.readline()
for i in range(int(testcase)):
    line1 = sys.stdin.readline().rstrip()
    print("Case #{}: {}".format(i+1, solution(line1)))