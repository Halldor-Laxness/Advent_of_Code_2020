from functools import reduce
def loadData(path:str):
    with open(path) as file:
        lines = file.read().split()
    return int(lines[0]),[int(item) if item!='x' else 'x' for item in lines[1].split(',')]

def calculateWaitingTime(timestamp, busIds):
    minTime = float('inf')
    for id in busIds:
        if id == 'x':
            continue
        mod = 0 if timestamp%id==0 else id -timestamp%id
        if mod < minTime:
            minTime = mod
            busId = id
    return busId*minTime

def findMatchingTimestamp(busIds):
    seqs = []
    ids = []
    for seq, id in enumerate(busIds):
        if id == 'x': continue
        seqs.append((-seq)%id)
        ids.append(id)
    return chineseRemainderTheorem(ids,seqs)


def chineseRemainderTheorem(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mulInv(p, n_i) * p
    return sum % prod
 
def mulInv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

if __name__ == "__main__":
    timestamp, busIds = loadData("input.txt")
    print("Part 1:", calculateWaitingTime(timestamp, busIds))
    print("Part 2:", findMatchingTimestamp(busIds))
