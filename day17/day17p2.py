def processRawData(location):
    text = open(location)
    lines = text.readlines()
    lines = [line.rstrip() for line in lines]
    text.close()
    return [[lines]]

def simulatingCircles(data, number):
    for i in range(number):
        data = simulatingOneCircle(data)
    return data

def simulatingOneCircle(data):
    re4d = []
    for w in range(-1,len(data)+1):
        result = []
        for z in range(-1,len(data[0])+1):
            rows =[]
            for x in range(-1,len(data[0][0])+1):
                row = ""
                for y in range(-1,len(data[0][0][0])+1):
                    row += '#' if isActiveInNextCircle(w, z, x, y,data) else '.'
                rows.append(row)
            result.append(rows)
        re4d.append(result)
    return re4d

def isActiveInNextCircle(w, z, x, y, data):
    selfActiveStatus = isActiveNow(w,z,x,y,data)
    count = 0
    for wdim in range(w-1,w+2):
        for zdim in range(z-1,z+2):
            for xdim in range(x-1,x+2):
                for ydim in range(y-1,y+2):
                    if zdim == z and xdim==x and ydim==y and wdim==w:
                        continue
                    count += 1 if isActiveNow(wdim,zdim, xdim,ydim, data) else 0
    if selfActiveStatus:
        if count==2 or count==3:
            return True
    else:
        if count==3:
            return True
    return False

def isActiveNow(w,z,x,y,data):
    if w<0 or w>=len(data)or z<0 or x<0 or y<0 or z>=len(data[0]) or x>=len(data[0][0]) or y>=len(data[0][0][0]):
        return False
    else:
        return True if data[w][z][x][y] == '#' else False

def countActiveCubes(data):
    count = 0
    for lists in data:
        for li in lists:
            for item in li:
                count  += item.count('#')
    return count
     
if __name__ == "__main__":
    data = processRawData("input.txt")
    result = simulatingCircles(data,6)
    print("Part 2:",countActiveCubes(result))
                 
