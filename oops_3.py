class Circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi

    def get_circum(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(30)
print(my_circle.area)
print(my_circle.get_circum())