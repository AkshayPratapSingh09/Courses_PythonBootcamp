# Soruce = https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/00-Python%20Object%20and%20Data%20Structure%20Basics/09-Objects%20and%20Data%20Structures%20Assessment%20Test.ipynb)

a = [1,2,[3,4,'Hello']]
a.pop(2)
a.append([3,4,'Goodbye'])
print(a)

b = [5,3,4,6,1]
b.sort()
print(b)

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1])

#Will not work cause dictionary are made to store only 1 key value
# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# d.sort()
# print(d)

a = (1,2,3,4,5)
print(type(a))

list5 = [1,2,2,33,4,4,11,22,3,3,2]
c = set(list5)
print(c)
print(type(c))


