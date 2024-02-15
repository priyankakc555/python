#jan25
# tuples are also the interables in python (like list, string and set)
# tuples are immutabke datatypes
#tuple elements are enclosed inside small brackets

#creating tuples
a=() # empty tuple
b= tuple() # empty tuple


list(),set(),tuple(),int(),float(),bool(),str() #these are built in functions for datatypes

c=(1,2,3) #non empty tuple
#elements can be of mixed datatype
d = (1, 2.1, "hello", [1, 2])


# Accessing tuple elements
# Tuple elements can also be accessed using Indexing and Slicing similar to list
vowels = ("a", "e", "i", "o", "u")
print(vowels[0])  # a
print(vowels[-1])  # u

print(vowels[:2])  # ("a", "e")
print(vowels[3:])  # ("o", "u")
print(vowels[4:2])  # ()