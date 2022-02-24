a = int(input("Enter number: "))
list1 = []
for i in range(1, a): 
    if (a%i == 0):
        list1.append(i)
    
print(list1)