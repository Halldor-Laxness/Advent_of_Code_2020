class Ship:
    def __init__(self):
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]
        self.directMap = {'N':0,'E':1,'S':2,'W':3}
        self.shipLoc = [0,0]
        self.waypoint = [10,1]

    def changeDirect(self, turn, degree):
        if turn =='L':
            for i in range(degree//90):
                carbon = self.waypoint.copy()
                self.waypoint[0] = 0-carbon[1]
                self.waypoint[1] = carbon[0]
        else:
            for i in range(degree//90):
                carbon = self.waypoint.copy()
                self.waypoint[0] = carbon[1]
                self.waypoint[1] = 0-carbon[0]

    def moveTowards(self, direction, distance):
        if direction in self.directMap:
            curDirect = self.directions[self.directMap[direction]]
            self.waypoint[0] += curDirect[0]*distance
            self.waypoint[1] += curDirect[1]*distance
        elif direction=='L' or direction =='R':
            self.changeDirect( direction, distance)
        else:
            self.shipLoc[0] += self.waypoint[0]*distance
            self.shipLoc[1] += self.waypoint[1]*distance

    def executeIntructs(self,intructs):
        for instruct in intructs:
            self.moveTowards(instruct[0], int(instruct[1:]))

    def calculateManhattanDis(self):
        return abs(self.shipLoc[0])+abs(self.shipLoc[1])

    @staticmethod
    def loadData(path:str):
        with open('input.txt') as file:
            return file.read().split()

if __name__=="__main__":
    ship = Ship()
    instructs = ship.loadData('input.txt')
    ship.executeIntructs(instructs)
    print("Part 2: ", ship.calculateManhattanDis())
