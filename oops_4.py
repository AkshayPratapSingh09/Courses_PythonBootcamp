class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self): 
        print("I am eating")

# myanimal = Animal()
# print(myanimal.eat())

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("Whoo!")

    def eat(self):
        print("I am dog and i am eating!!")

mydog = Dog()
print(mydog.bark())
# print(mydog.who_am_i())


