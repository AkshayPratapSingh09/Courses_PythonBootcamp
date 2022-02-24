
#Will print numbers from 0 to 4
x = 0 
while x<5:
    print(f"The current value of x is {x}")
    x = x+1


#Alternate method
x = 50 
while x<5:
    print(f"The current value is {x}")
    x += 1
else:
        print("The value is 5 now")

#Loop in Dictionary
dict1 = {(1,2), (2,3), (3,5),(7,8)}
for set in dict1:
    print(set)

for (a,b) in dict1:
    print(a)
    print(b)

x = [1,23,3,4,35]
for item in x:
    print("The way is far")
    pass
print('End of the disccusion')

#Will print letter except "a"
mystring = "Sammy"
for letter in mystring:
    if letter  == "a":
        continue
    print(letter)

#Will break the function on "a" 
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
 

#Will print number from 0 to 4
x =0 
while x < 5:
    print(x)
    x += 1

    
#Will break the fucntion on 2
x =0 
while x < 5:
    if x ==2:
        break
    print(x)
    x += 1
