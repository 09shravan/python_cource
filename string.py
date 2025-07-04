name="shravan"
friend="pranjal"

print("hello,"+name)
# if you want to add two strings together then use + operator #

print("hello,"+name+friend)


apple=("i love apple to eat everyday")
print(apple)

name="mango"            # string slicing and operations #
print(name[0:4])
print(name[1:4])
print(name[:])
print(name[0:-3])


# strings methods in python or string handling #


name="shravan"


print(len(name))
print(name.upper())
print(name.lower())

intro="my name is shravan and i am an is a  a data scientist"
print(intro.capitalize())
print(intro.center(89))
print(intro.count("a"))
print(intro.find("data"))

intro="my name is shravan and i am an is a  a data scienti/n"
print(intro.isalnum())
print(intro.isalpha())
print(intro.isprintable())