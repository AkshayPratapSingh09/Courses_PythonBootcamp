#Sets
myset = set()
myset.add(1)
myset.add(2)
print(myset)

myset.add(2)
myset.add(4) #-->Will not work cause sets has each unique value cant repeat
print(myset)

a = [1,33,33,23,456,12,2,456,1,1,1,76]
b=set(a)
c = b.sort()
print(c)