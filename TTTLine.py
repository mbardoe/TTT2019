from TTTPoint import *

class TTTLine(object):
    def __init__(self, points):
        super(TTTLine, self).__init__()
        self.points=points


    def __str__(self):
        ret=""
        for point in self.points:
            ret+=str(point)+", "
        return ret[:-2]

    def __eq__(self, o):
        return self.points==o.points

    def __repr__(self):
        return str(self)

    def pointOnLine(self, point):
        return point in self.points

    def __iter__(self):
        return self.points.__iter__()


if __name__ == "__main__":
    x=TTTPoint([0,0,0])
    y=TTTPoint([1,0,-1])
    z=TTTPoint([-1, 0, 1])
    line=TTTLine([x,y,z])
    print(line)
    line2=TTTLine([z,x,y])
    print("Is line equal to line2")
    print(line==line2)

