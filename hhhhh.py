a=int(input("enter a value: "))
rev=0
while (a>0):
    rev=(rev*10)+a%10
    a=a//10

    
if (rev!=a):
           print("reverse of your entered number is",rev)
else:
    print("given numberis a pellindrome")        


