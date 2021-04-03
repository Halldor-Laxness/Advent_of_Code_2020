def countTree( data , horizontal, vertical):
    start = 0
    width = len(data[0]) - 1
    count = 0
    for i in range(0, len(data), vertical):
        start = start % width
        if data[i][start] == "#":
            count+=1
        start += horizontal
    return count

def processRawData(location):
    text = open(location)
    lines = text.readlines()
    text.close()
    return lines

if __name__ == "__main__":
    data = processRawData("input.txt")
    count = countTree(data, 3, 1) * countTree(data,1,1) * countTree(data, 5, 1) *countTree(data, 7,1)*countTree(data,1,2)
    print("tree count:", count)
