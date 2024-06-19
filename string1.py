# string is immutable
t = "h        trisha srivastAva is a girl .\n But  \'french \\trish'a a \t dude            "
 # \n for next line and \t for a tab \' to print a ' and \\ to print \
t1='                      str                '
#  ***********************   string is immutable   **************************

print(t[1])
print(t[1:5]) #this does not include the second index
print(t[::3]) # starts with 0 and jumps 3 spaces
print(t1.strip()) # removes extra space
# ^^^^^^^^^^^^^^^^^^^^IMPORTANT^^^^^^^^^^^^^^^^^^^

print(t[::-1]) #helps in reversing the string
print(t[1:]) # replaces with length
g=t[-5:-1]
print(g)
h= t[0:8:2] # starts with 0 print excluding 8 and print every "2nd" in the sequence
print(h)
print(len(t))
print(t.endswith("tava")) #bool function return if string ends with this string
print(t.endswith("qwerty"))
print(t.count("s")) #counts no of times character/string has occured
print("capitalizes the first letter and changes rest to lower letters",t.capitalize()) # capitalizes the first letter
print(t.find("sri")) #returns the index of the first occurence where the string starts
print(t.replace("trisha","timothee")) # replaces the word every where
# removes extra space from the string 
t1=t.split() #returns a list
print(t1)
t2=' '.join(t1)
print(t2)
t3=t.rsplit("a") # returns a copy of the string with trailing characters removed
#(based on the string argument passed). If no argument is passed, it removes trailing spaces.
print(t3) 
var="this is a string"
var1=3.12456
print("Hello did you know {} and a {:.3f}" .format(var,var1))
print(f"Hello did you know {var} and a {var1:.3f}")

#.string.isalnum checks to find if string is alphanumeric and returns true or false
#string.isalpha checks if there are any numbers in the string
# string.isprintable checks if all the characters are printable in the string(non printable characters e.g \n)
# string.isspace checks if any space bar has been used in the string