my_list = ["1", "2", "3"]
my_list1 = [5,100,23]
a=len(my_list)               #Will print the amount of data the set have
print(a)

# # Slicing in A Set
print(my_list[0])


new_list = my_list + my_list1
print(new_list)  

#Adding Item to the list (Will substitute the numbers)
new_list[0] = 19
print(new_list)

# new_list[6] = 24
# print(new_list)   #Not possible to change the values not in the list

#For the above operation we need another function(Has the ability to add new values to the list)
new_list.append('new number')
print(new_list)


#Can remove items from the set(By default will remove the last digit)
new_list.pop()
print(new_list)

#For any specific value removal
new_list.pop(2)
print(new_list) 


my_list = [2,3,4,5,6]
print(my_list[2:])
another_list = ["one","two","three","four"]
print(another_list)

new_list = my_list + another_list
new_list[0]='One all Caps'

#AppendFunction will add the values in the end of the list
print(new_list)
new_list.append('six')
print(new_list)

new_list.append('seven')
print(new_list)

#Will remove entry from the list
new_list.pop(6)
print(new_list)


popped_item = new_list.pop(2)
print(new_list)

new_list2=['a','x','f','r','e','d','s']

#will sort the values in an order
new_list2.sort()
print(new_list2)

mysorted_list = new_list2.sort()
print(mysorted_list)

new_list2.sort()
mysorted_list = new_list2
print(mysorted_list)

#Will Reverse the whole list First to last 
new_list.reverse()
print(new_list)

