# class sample():
#     pass


# mysample = sample()
# print(type(mysample))
# my_dog = Dog(mybreed="Husky")
# # dog( )  = sample()
# def __init_(self,breed):

# # print(square.__doc)
# print(type(my_dog))

# mylist = [1,2,5,3,4]
# myset = set()
# class Sample():
#     pass
# mysample = Sample()
# print(type(mysample))

class Dog():
    def __init__(self,mybreed,name,spots): #init is the constructor of the class
        #Attribute
        #we take in the argument
        #assign it using self.attribute_name
        self.breed = mybreed
        self.name = name

        #expect boolean true/false
        self.spots = spots


my_dog = Dog(mybreed = "lab",name="Vicky",spots=False)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)


