class Ship:
    def __init__(self):
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.direct = 1
        self.directMap = {'N':0,'E':1,'S':2,'W':3}
        self.location = [0,0]

    def changeDirect(self, turn, degree):
        if turn =='L':
            self.direct = (self.direct+4-degree//90)%4
        else:
            self.direct = (self.direct+degree//90)%4

    def moveTowards(self, direction, distance):
        if direction in self.directMap:
            curDirect = self.directions[self.directMap[direction]]
            self.location[0] += curDirect[0]*distance
            self.location[1] += curDirect[1]*distance
        elif direction=='L' or direction =='R':
            self.changeDirect( direction, distance)
        else:
            curDirect = self.directions[self.direct]
            self.location[0] += curDirect[0]*distance
            self.location[1] += curDirect[1]*distance

    def executeIntructs(self,intructs):
        for instruct in intructs:
            self.moveTowards(instruct[0], int(instruct[1:]))

    def calculateManhattanDis(self):
        return abs(self.location[0])+abs(self.location[1])

    @staticmethod
    def loadData(path:str):
        with open('input.txt') as file:
            return file.read().split()

if __name__=="__main__":
    ship = Ship()
    instructs = ship.loadData('input.txt')
    ship.executeIntructs(instructs)
    print("Part 1: ", ship.calculateManhattanDis())
