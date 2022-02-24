def hello(name="rose"):
    print("The hello() function has been executed!!")

    def greet():
        return "\t This is greet() function under the hello!!"

    def welcome():
        return "This is welcome() inside hello"

    print("This is the end of the function!!")

# print(hello())
# print(greet())
# print(welcome())
    if name =="Rose":
        return greet
    else:
        return welcome

my_new_func = hello("Jose")
print(my_new_func())