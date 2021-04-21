def findNthNum(starts, n):
     dictionary = {key:val for val,key in enumerate(starts)}
     return findNthNumHelper(dictionary, starts[-1], n)

def findNthNumHelper(curDict,curNum,targetTurn):
    prevDict = {}
    for i in range(len(curDict),targetTurn):
        if curNum in prevDict:
            curNum = curDict[curNum]-prevDict[curNum]
        else:
            curNum = 0
        if curNum in curDict:
            prevDict[curNum] = curDict[curNum]
        curDict[curNum] = i
    return curNum

if __name__ == "__main__":
    print("Part 1:",findNthNum([0,14,6,20,1,4],2020))
    print("Part 2:",findNthNum([0,14,6,20,1,4],30000000))
