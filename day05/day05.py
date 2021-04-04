def parseSeat(string: str)->int:
    rows = string[0:7]
    cols = string[7:10]
    row = binaryParse(rows)
    col = binaryParse(cols)
    return row*8+col

def binaryParse(string:str)->int:
    low = 0
    high = 2**len(string)-1
    for i in range(len(string)):
        cha = string[i]
        if(cha=="L" or cha =="F"):
            high = (low+high)//2
        elif(cha == "R" or cha == "B"):
            low = (low+high)//2+1
    return low

def processRawData(location):
    text = open(location)
    lines = text.readlines()
    text.close()
    return lines

def checkHighestId(data):
    highest = float('-inf')
    for line in data:
        current = parseSeat(line)
        if current > highest:
            highest = current
    return highest

def locateMySeat(data):
    seatOccupation = [0]*(128*8)
    for line in data:
        current = parseSeat(line)
        seatOccupation[current] = 1
    for i in range(1,len(seatOccupation)):
        if(seatOccupation[i]==0 and seatOccupation[i-1]==1 and seatOccupation[i+1]==1):
            return i
    return -1

if __name__ == "__main__":
    data = processRawData("input.txt")

    highestId = checkHighestId(data)
    print("highest ID: ", highestId)

    mySeat = locateMySeat(data)
    print("my seat: ", mySeat)

