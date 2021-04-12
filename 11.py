def processRawData(location):
    text = open(location)
    lines = text.readlines()
    text.close()
    lines = [[char for char in line.rstrip()]for line in lines]
    return lines

def getFinalState(data,method):
    stateChanged = 1
    while stateChanged>0:
        result = []
        stateChanged = 0
        for i in range(len(data)):
            row = []
            for j in range(len(data[i])):
                statusChange = method(i,j,data)
                if statusChange:
                    row.append('L' if data[i][j]=='#' else '#')
                    stateChanged += 1
                else:
                    row.append(data[i][j])
            result.append(row)
        #print(result)
        data = result
    return data

def isChangedV2(i,j,data):
    if data[i][j]=='.':  return False
    count = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    for direct in directions:
        x = i+direct[0]
        y = j+direct[1]
        while x>=0 and y>=0 and x<len(data) and y<len(data[0]) and data[x][y]=='.':
            x = x+direct[0]
            y = y+direct[1]

        if x>=0 and y>=0 and x<len(data) and y<len(data[0]) and data[x][y]=='#':
            count+=1
    if (data[i][j] =='L' and count ==0) or (data[i][j]=='#' and count>=5):
        return True
    else:
        return False

def isChangedV1(i,j, data):
    if data[i][j]=='.':  return False
    count = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    for direct in directions:
        x = i+direct[0]
        y = j+direct[1]
        if x>=0 and y>=0 and x<len(data) and y<len(data[0]) and data[x][y]=='#':
            count+=1
    if (data[i][j] =='L' and count ==0) or (data[i][j]=='#' and count>=4):
        return True
    else:
        return False

def countOccupied(data):
    count = 0
    for row in data:
        for seat in row:
            if seat =='#':
                count+=1
    return count
if __name__ == "__main__":
    data = processRawData("day11.in")
    resultV1 = getFinalState(data,isChangedV1)
    print("part 1:", countOccupied(resultV1))
    resultV2 = getFinalState(data,isChangedV2)
    print("part 2:", countOccupied(resultV2))