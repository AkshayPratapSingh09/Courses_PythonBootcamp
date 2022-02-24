#Tuple
a = (1,2,3,4,5)
print(type(a))

t =('a','a','b','c')
#Count the number of occurence of the word
c= t.count('a') 
print(c)

#Will tell  the first location of the word
c= t.index('a') 
print(c)

c= t.index('b') 
print(c)

#Tuples are immutatable
# t[0] = "2"
# print(t)