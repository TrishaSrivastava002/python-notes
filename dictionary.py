t= {
    "tree" : "things that grow on soil",
    "mango" : "a fruit",
    "marks" : [1,2,3,4],
    "p" : 4,
    3: 6,
    "books" : {"harry" : "potter"}
    #key          value
}
d=dict(tish="srivas",anna="addams",col="mikel")

del d["tish"] # used to delete an element
print(d.keys())
print(d.values())
print(d.items())

print(t['tree'])
print(t['marks'])
print(t['p'])
print(t['books']['harry'])
t['marks'] = [5,6,7,8] #replaces the earlier values
t['mango'] = "yummy"
print(t['mango'])     #gives same value but gives error if element is not present
print("Get: ",t.get("orange")) #gives same value but throws error element if element is not present
print(t['mango'])
print(t.keys())
print(list(t.keys())) #type casted as list
print(t.items()) #prints key,value pair
print(t)
up = { "paneer" : "love", "queen" : "king","p" : 8 } #updates the list if a key is repeated
t.update(up)
print(t)
print(t.get("p"))
print(t.clear()) #clears the whole data in dictionary    

#In dictionary if we use mydict["marks"] to access the value at the key marks it will throw 
# an error if marks is not a key so it's our responsibility to give correct key but when we use
#  mydict.get("marks") it will return none if key is not present

# 2 ways to copy a dictionary 
# 1 method changes both original and copied dictionary   
d1=d
d1["tish"]="Liester"
print(d1)
print(d)
# 2 method does not changes the original dictionary
d2=d.copy()
d2["tish"]="Langdon"
print(d2)
print(d)
