import sys

class Grid:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
        self.left = None
        self.right = None

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left
        self.data = None
    
    def deleted(self):
        return self.data == None
    
    def smaller(self):
        comp = []
        if self.left:
            comp.append(self.left.data)
        if self.prev:
            comp.append(self.prev.data)
        if self.right:
            comp.append(self.right.data)
        if self.next:
            comp.append(self.next.data)
        
        if len(comp) == 0:
            return False
        return (sum(comp)/len(comp)) > self.data
    
    def __str__(self):
        return "Grid({})".format(self.data)
    
def toGraph(arr):
    colTemp = [None for _ in arr[0]]
    for y, line in enumerate(arr):
        temp = None
        for x, v in enumerate(line):
            node = Grid(v)
            node.left = temp
            node.prev = colTemp[x]
            if temp:
                temp.right = node
            if colTemp[x]:
                colTemp[x].next = node
            temp = node
            colTemp[x] = node
    temp = colTemp[0]
    while temp.prev:
        temp = temp.prev
    return temp

def solution(arr):
    eliminate = []
    graph = toGraph(arr)
    remain = 0
    acc = 0
    yiter = graph
    while yiter:
        xiter = yiter
        while xiter:
            remain = remain + xiter.data
            if xiter.smaller():
                eliminate.append(xiter)
            xiter = xiter.right
        yiter = yiter.next
    
    acc = remain
    stack = [eliminate]
    while len(stack) > 0:
        lastround = stack.pop(0)
        if len(lastround) == 0:
            break
        temp = []
        leave = 0
        check_set = set()
        for dancer in lastround:
            leave = leave + dancer.data
            dancer.delete()
            check_list = [dancer.left, dancer.right, dancer.prev, dancer.next]
            for c in check_list:
                if c and not c.deleted():
                    check_set.add(c)
        for c in check_set:
            if c and not c.deleted() and c.smaller():
                temp.append(c)

        remain = remain - leave
        acc = acc + remain
        stack.append(temp)

    return acc
                
        

line = sys.stdin.readline()
for i in range(int(line)):
    line = sys.stdin.readline()
    [r, c] = [ int(x) for x in line.rstrip('\n').split(' ') ]
    buffer = []
    for _ in range(r):
        line = sys.stdin.readline()
        buffer.append([ int(x) for x in line.rstrip('\n').split(' ') ])
    
    print("Case #{}: {}".format(
        i + 1,
        solution(buffer)
    ))
