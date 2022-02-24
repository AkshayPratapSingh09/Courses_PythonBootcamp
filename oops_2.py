# class Dog():

#     #Class object attribute
#     #Same for any instance of a class
#     species = "Mammal"
#     def __init__(self,mybreed,name): #init is the constructor of the class
#         #Attribute
#         #we take in the argument
#         #assign it using self.attribute_name
#         self.mybreed = mybreed
#         self.name = name

#     def bark(self,number):
#         print("Woof! My name is {} and the number is {}".format(self.name,number))

# my_dog = Dog("Lab","Frankie")
# print(my_dog.bark(10))
        


# Diff between a method and a function
#--> Method is a function inside a class
#Operations/Actions ---> Method

class Animal:

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am a animal")

    def eat(self):
        print("I am eating")

