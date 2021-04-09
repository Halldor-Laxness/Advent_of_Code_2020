def processRawData(location,dimension):
    text = open(location)
    lines = text.readlines()
    lines = [[char for char in line.rstrip()] for line in lines]
    text.close()
    for i in range(dimension-2):
        lines = [lines]
    return lines

def simulatingCircles(path, dimension, number):
    data = processRawData(path,dimension)
    for i in range(number):
        data = simulatingOneCircle(data,1,dimension,list())
    return data

def simulatingOneCircle(data, curDimension, targetDimension, processedDim):
    result = []
    if (curDimension==targetDimension):
        result.append('#' if isActiveInNextCircle(data, processedDim.copy()) else '.')
        return result

    data4Len = data
    for i in range(curDimension):
        data4Len = data4Len[0]
    for w in range(-1,len(data4Len)+1):
        print(w)
        print(processedDim)
        newDim = processedDim.copy()
        newDim.append(w)
        result.append(simulatingOneCircle(data, curDimension+1, targetDimension, newDim))
    return result

def isActiveInNextCircle(data, dimensions):
    selfActiveStatus = isActiveNow(data,*dimensions)
    count = isNeghborsActive(data,list(dimensions),[])
    if selfActiveStatus:
        if count==1 or count==2:
            return True
    else:
        if count==3:
            return True
    return False

def isNeghborsActive(data, curLoc, neighborLoc):
    if len(curLoc)>0:
        curDimension = curLoc.pop(0)
        nextNeighborLoc1 = neighborLoc.copy()
        nextNeighborLoc1.append(curDimension-1)
        nextNeighborLoc2 = neighborLoc.copy()
        nextNeighborLoc2.append(curDimension)
        nextNeighborLoc3 = neighborLoc.copy()
        nextNeighborLoc3.append(curDimension+1)
        return isNeghborsActive(data, curLoc.copy(), nextNeighborLoc1)+isNeghborsActive(data, curLoc.copy(), nextNeighborLoc2)+isNeghborsActive(data, curLoc.copy(), nextNeighborLoc3)
    else:
        return 1 if isActiveNow(data,*neighborLoc) else 0


def isActiveNow(data, *dimensions):
    for dim in dimensions:
        if dim >=0 and dim <len(data):
            data = data[dim]
        else:
            return False
    return True if data == '#' else False

def countActiveCubes(data):
    count = 0
    for lists in data:
        for li in lists:
            for item in li:
                count  += item.count('#')
    return count
     
if __name__ == "__main__":
    # data = processRawData("input.txt")
    # result = simulatingCircles(data,6)
    print("Part 2:",simulatingCircles("input.txt",3,3))
                 
