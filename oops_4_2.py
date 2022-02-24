from playsound import playsound

class Dog():
    
    def __init__(self,name):
        self.name = name
        self.sound = playsound('C:\\Users\\ApS\\Desktop\\Python\\Python1.0\\OOPS\\bark.mp3')

    def speak(self):
        return self.name + " says woof!"
        return self.sound  

class Cat():

    def __init__(self,name):
        self.name = name
        self.sound = playsound('C:\\Users\\ApS\\Desktop\\Python\\Python1.0\\OOPS\\cat.mp3')

    def speak(self):
        return self.name + " says meow!"
        return self.sound 

Munmun = Dog("Munmun")
Dopa = Cat("Dopa") 
print(Munmun.speak())
print(Dopa.speak())

for pet in [Munmun,Dopa]:

    print(type(pet))
    print(pet.speak())

class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
# myanimal = Animal("fred")
# myanimal.speak()

fido = Dog("fido")
isis = Cat("Isis")
print(fido.speak())