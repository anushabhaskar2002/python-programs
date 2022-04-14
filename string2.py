#join()
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


#just()
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

#lower()
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#istrip()
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")


#maketrans()
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

#partition()
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

#replace()
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#rfind()
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

#rindex()
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

#rjust()
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

#rpartition()
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

#rsplit()
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

#rstrip()
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

#split()
txt = "welcome to the jungle"

x = txt.split()

print(x)

#splitlines()
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

#startswith()
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

#strip()
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

#swapcase()
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

#title()
txt = "Welcome to my world"

x = txt.title()

print(x)

#translate()
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#upper()
txt = "Hello my friends"

x = txt.upper()

print(x)

#zfill()
txt = "50"

x = txt.zfill(10)

print(x)
