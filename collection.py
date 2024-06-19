# types of tuples
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# counts the occurence of each character
a="aasbbbjjjttmmmm"
count=Counter(a)
print(count)
print(count.keys())
print(count.values())
print(count.most_common())
print(count.most_common(1)) # there can be multiple keys with same highest values so it returns a list
print(count.most_common(1)[0])
print(count.most_common(1)[0][0])
print(count.most_common(2))
print(list(count.elements()))

# helps generate named tuple can be understood as a list
point=namedtuple('point','x y')
pt=point(6,7)
print(pt.x,pt.y)
# remembers the order of insertion of key and value pair 
ord=OrderedDict()
ord["b"]=2
ord["c"]=3
ord["a"]=1

print(ord)

# does not raise error on getting a key which is not a part of the dictionary
df=defaultdict(int)
df["b"]=2
df["c"]=3
df["a"]=1
print(df)
print(df["a"])
print(df["d"])



d=deque()
d.append(1)
d.append(56)
d.appendleft(12)
d.appendleft(90)
d.extendleft([89,88,87]) # first 89 will be appended then 88, then 87
d.rotate(1)
print(d)
d.pop()
d.popleft()
print(d)
d.clear()
print(d)