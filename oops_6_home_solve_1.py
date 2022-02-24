class Simple():
        
    def __init__(self,value):
        self.value = value

    def add_to_value(self,amount):
        self.value = self.value + amount

myobj = Simple(300)

print(myobj.value)

myobj.add_to_value(50)

print(myobj.value)


