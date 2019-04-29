from TTTPoint import *
from TTTLine import *


class ThreeDTTT(object):
    def __init__(self, size):
        super(ThreeDTTT, self).__init__()
        self.size = size
        self.points = []
        self.lines = []
        self.maxCoord = self.size / 2
        for i in xrange(-self.maxCoord, self.maxCoord + 1, 1):
            for j in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                for k in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                    self.points.append(TTTPoint([i, j, k]))
        self.__construct_lines___()

    def __construct_lines___(self):
        # plane x
        # vertical & horizontal lines
        for k in xrange(-self.maxCoord, self.maxCoord + 1, 1):
            # k=0
            for i in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                vertpointsonline = []
                horpointsonline = []
                for j in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                    vertpointsonline.append(TTTPoint([k, i, j]))
                    horpointsonline.append(TTTPoint([k, j, i]))
                self.lines.append(TTTLine(vertpointsonline))
                self.lines.append(TTTLine(horpointsonline))
            # diagonal lines
            maindiagline = []
            altdiagline = []
            for i in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                maindiagline.append(TTTPoint([k, i, i]))
                altdiagline.append(TTTPoint([k, -i, i]))
            self.lines.append(TTTLine(maindiagline))
            self.lines.append(TTTLine(altdiagline))
        # plane y
        for k in xrange(-self.maxCoord, self.maxCoord + 1, 1):
            for i in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                pointsonline = []
                for j in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                    pointsonline.append(TTTPoint([j, k, i]))
                self.lines.append(TTTLine(pointsonline))
            # diagonal lines
            maindiagline = []
            altdiagline = []
            for i in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                maindiagline.append(TTTPoint([i, k, i]))
                altdiagline.append(TTTPoint([-i, k, i]))
            self.lines.append(TTTLine(maindiagline))
            self.lines.append(TTTLine(altdiagline))
        # plane z
        for k in xrange(-self.maxCoord, self.maxCoord + 1, 1):
            # diagonal lines
            maindiagline = []
            altdiagline = []
            for i in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                maindiagline.append(TTTPoint([i, i, k]))
                altdiagline.append(TTTPoint([-i, i, k]))
            self.lines.append(TTTLine(maindiagline))
            self.lines.append(TTTLine(altdiagline))
        # largest diagonals
        maindiagline = []
        altdiagline1 = []
        altdiagline2 = []
        altdiagline3 = []
        for k in xrange(-self.maxCoord, self.maxCoord + 1, 1):
            maindiagline.append(TTTPoint([k, k, k]))
            # (-1,1,-1),(0,0,0),(1,-1,1)
            altdiagline1.append(TTTPoint([k, -k, k]))
            altdiagline2.append(TTTPoint([-k, k, k]))
            altdiagline3.append(TTTPoint([k, k, -k]))
        self.lines.append(TTTLine(maindiagline))
        self.lines.append(TTTLine(altdiagline1))
        self.lines.append(TTTLine(altdiagline2))
        self.lines.append(TTTLine(altdiagline3))

    def displayWins(self, moves=[]):
        ans=''
        for i in xrange(-self.maxCoord, self.maxCoord + 1, 1):
            for j in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                for k in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                    currentPoint=TTTPoint([i,j,k])
                    ans+=str(self.countwinlines(currentPoint,moves)) + '\t'
                ans+="\n"
            ans+="\n"
        ans+="\n\n"
        print ans

    def displayGame(self, playerOneMoves, playerTwoMoves=[]):
        ans = ''
        for i in xrange(-self.maxCoord, self.maxCoord + 1, 1):
            for j in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                for k in xrange(-self.maxCoord, self.maxCoord + 1, 1):
                    if TTTPoint([i, j, k]) in playerOneMoves:
                        ans += 'x' + '\t'
                    elif TTTPoint([i, j, k]) in playerTwoMoves:
                        ans += 'o' + '\t'
                    else:
                        ans+='_'+'\t'
                ans += "\n"
            ans += "\n"
        ans += "\n\n"
        return ans

    def winner(self,moves):
        for lines in self.lines:
            for point in line:
                if not point in line:
                    break
                return True
        return False

    def countwinlines(self, point, moves=[]):
        ans = 0
        #moves=set(moves)
        for line in self.lines:
            if len([x for x in moves if x in line])==0:
                if line.pointOnLine(point):
                    ans += 1
        return ans

    def __str__(self):
        return self.size

    def __eq__(self, o):
        return self.size == o.size


if __name__ == "__main__":
    x = ThreeDTTT(3)
    print(len(x.points))
    print(len(x.lines))
    # for line in x.lines:
    #     print(line)
    for point in x.points:
        print(str(point) + " " + str(x.countwinlines(point)))
    center=TTTPoint([0,0,0])
    x.displayWins([center])
    print(x.countwinlines(center,[center]))