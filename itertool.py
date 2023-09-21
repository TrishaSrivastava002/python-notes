from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import accumulate
import operator
from itertools import groupby

# product
a=[2,3]
b=[4,5]
print(list(product(a,b)))
print("\n")
print(list(product(a,b,repeat=2)))
print("\n")
print("\n")

# permutations
c=[1,2,3,4]
print(list(permutations(c)))
print("\n")
# takes only 3 inputs 
print(list(permutations(c,3)))
print("\n")

# combinations
d=[1,2,3,4]
print(list(combinations(d,2)))
print("\n")
print(list(combinations_with_replacement(d,2)))
print("\n")

# accumulator
e=[1,2,3,5,0,6,4]
print(list(accumulate(e)))
print("\n")
print(list(accumulate(e))[2])
print("\n")
print(list(accumulate(e, func=operator.mul)))
print("\n")
print(list(accumulate(e,func=max)))
print("\n")

# groupby
def solve(x):
    return x<3
g=[5,2,4,1,0,10]
gift=groupby(g,key=solve)
for key,value in gift:
    print(key,list(value))
print("\n")



