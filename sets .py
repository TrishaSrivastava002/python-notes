
v = set() # an empty set it does not contain duplicates and the order is arbitrary it does not throw error if 
# element is not found
# set is mutable and is unordered i.e, does not follows the order of data stored 
print(type(v))
v.add(4)
v.add(14)
v.add(24)
v.add((1,2,3)) #tuple can be added in set 
print(v)
v.remove(14) # in place of remove we can also use the discard function which does not raise an error of the element too be removed 
#is not found
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
s6=s1.symmetric_difference(s2) #returns the elements of the set which are not present in the other set 
# i.e removes the common elements of the sets are combines them
print(s6) # similarly we can use disjoint , difference_update issuperset, and other set operations

s7=s1.update(s2)
print(s7) # combines the 2 sets without repeating the elements

s8=s1.intersection_update(s2)
print(s8) # returns only the element taht are  present in both the sets

s9=s1.difference_update(s2)
print(s9) # returns s1 after removing common elements that are ppresentt in s2

s10=s1.symmetric_difference_update(s2)
print(s10) # combines the 2 sets without repeating the elements present in both of them

print(s1.issubset(s2)) # tells if s1 is subset of s2
print(s1.issuperset(s2)) # tells if s1 is superset of s2
print(s1.isdisjoint(s2)) # tells if s1 is disjoint of s2

s11=s10.copy() #  used to copy a set
s12=set(s11) # another way used to copy a set

a=frozenset([1,2,3]) #immutable version of a set


