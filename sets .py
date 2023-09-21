
v = set() # an empty set it does not contain duplicates and the order is arbitrary it does not throw error if 
# element is not found
# set is immutable and is not ordered i.e, does not follows the order of data stored 
print(type(v))
v.add(4)
v.add(14)
v.add(24)
v.add((1,2,3)) #tuple can be added in set 
print(v)
v.remove(14)
print(v)
v.pop() #removes any element but through pop we can access the popped elements
print(v)
print(len(v)) # gives length of set
#set is a non repetitive list which can be updated, list and dict cannot be added 
s= {12,12.0,"12"}
print(type(s))
print(len(s)) # prints 2 becoz python considers 12 and 12.0 equal
p= {} # this an empty dictionery
p = set() # this is an empty set
print(type(p)) 
''' v.union/intersection returns sum of 2 sets and intersection returns the common elements'''
k= input("Enter K")
l=input("Enter L")
m= input("Enter M")
fav = {} 
fav['tri'] = k
fav['pri'] = l
fav['fri'] = m
print(fav)

'''In set if 20 and 20.0 are the only two values then the length of the set
 will be 1 as python considers it single value '''
s1={1,3,5,7,9}
s2={1,3,5,2,4,6,8,10}
# In Python, you cannot use the extend() method with sets because sets are unordered collections
#  of unique elements, and the extend() method is designed for ordered collections like lists. 
# The extend() method is used to add multiple elements from an iterable (like a list or tuple) to 
# the end of a list. 
s3=s1.union(s2) 
print(s3)
s4=s1.intersection(s2) 
print(s4)
s5=s1.difference(s2) 
print(s5)
s6=s1.symmetric_difference(s2) 
print(s6)
# similarly we can use disjoint , difference_update issuperset, and other set operations