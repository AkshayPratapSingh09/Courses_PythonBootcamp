class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        # return "The distance is" + self.distance

    def slope(self):

        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return (y2-y1)/(x2-x1)
        # return "The slope is " + self.slope

c1 = (1, 2)
c2 = (3, 4)

myline = Line(c1, c2)

print("The distance between the points is ", myline.distance())
print("The slope the line is ", myline.slope())
