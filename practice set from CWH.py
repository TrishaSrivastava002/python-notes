name = input()
print("good morning " +  name)

letter = '''hi my name is  |<NAME>| and date  is |<DATE>|
'''
print(letter)
name = input("enter name")
date = input("enter date")
letter = letter.replace("|<NAME>|", name)
letter = letter.replace("|<DATE>|", date)
print(letter)