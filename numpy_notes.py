import numpy as np

a=np.array([1,2,3])
print("array",a) 
# 3 elements but 1 Dimensional 
print("array shape",a.shape)
# num dimension (ndim)
print("array dimension",a.ndim)
# array datatype
print("array data type",a.dtype)
# array size 
print("array size",a.size)
# finds minimum
print(np.min(a))
# re constructs the matrix
print(a.reshape(3,1))
print("\n")
b=np.array([[1.1,2,3.5],[4.70,5,6.3],[7.90,8,9.2]])
print(np.vstack([a,b,a,b]))

# OUTPUT
# [[12 32]
#  [43  4]
#  [ 2  3]
#  [ 4  6]
#  [12 32]
#  [43  4]
#  [ 2  3]
#  [ 4  6]]
print("array",b)
print("array dimension",b.ndim)
# row>3 elements & col>3 Dimensional 
print("array shape",b.shape)
# array datatype
print("array data type",b.dtype)
# array size
print("array size",b.size)
# array second row
print("First row of b is",b[1,:])
# array second col
print("First row of b is",b[:,2])
b[1][1]=100.6
print(b)
print("\n")
print(np.zeros((2,3),dtype="int32"))
# array with any number filling the whole array
print(np.full((3,4),23))
# random number genrator
print(np.random.rand(4,2))
print(np.random.randint(12,64))
print(np.random.randint(12,64,size=(2,2)))

# when we try to copy an array like a into another array b then in python b(an array)=a(an array) means b will 
# start pointing to the address a was pointing to so it will change the array a if we make any changes to array b
# to copy an array 
c=a.copy()

# mathematical usage of numpy 
a=np.array([12,32,43,4])
print(a)
print(a/2)
print(a*2)
print(np.cos(a))

e=np.array([[12,32],[43,4]])
f=np.array([[12,32],[43,4]])
print(np.matmul(e,f))