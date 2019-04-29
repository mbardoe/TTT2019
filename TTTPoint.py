class TTTPoint(object):
    def __init__(self, coord):
        super(TTTPoint, self).__init__()
        self.coord=coord
        self.x=coord[0]
        self.y=coord[1]
        self.z=coord[2]

    def __str__(self):
        return str(self.coord)

    def __repr__(self):
        return str(self)

    def __eq__(self, o):
        return self.coord==o.coord

if __name__ == "__main__":
    x=TTTPoint([0,0,0])
    y=TTTPoint([1,0,-1])
    print("Is x equal to y?")
    print(x==y)
    print(x)
    print(y)

