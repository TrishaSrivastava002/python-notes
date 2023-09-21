from functools import reduce
l=lambda x:x+10
print(l(15))
# with 2 inputs
l=lambda x,y:x+10*y
print(l(15,12))
print("\n")
point=[(2,-3),(4,15),(6,-7),(8,9)] 
print(point)
print("\n")
point1=sorted(point,key=lambda x:x[1])
print(point1)
print("\n")
             
# mapping returns a map data type which implements a function on a list
ab=[2,3,5,6]
c=list(map(lambda x:x*12,ab))
d=[x for x in ab if x%2==0]
print("\n")
print("mapping c:\n",c)
print("\n")
print("mapping d:\n",d)
print("\n") 

# filtering returns a boolean data type for each element of an iterable and
#  if it's true the element is appended in the result 

e=filter(lambda x:x%2==0,ab)
print("Lambda function on d   :",d)
print("\nFiltering\n")
print(list(e))

#reduce returns a single value as a result of apply the given function 
print("\nReduce\n")
f=reduce(lambda x,y:x*y,ab)
print(f)

