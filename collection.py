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
print(count.most_common(1))
print(count.most_common(1)[0])
print(count.most_common(1)[0][0])
print(count.most_common(2))
print(list(count.elements()))

# helps generate named tuple
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
d.append(89)
d.pop()
d.popleft()
print(d)
d.clear()
print(d)