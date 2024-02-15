# Loops can be used in the datatypes which are iterables
# Iterable datatypes are list, string, tuple, set, dictionary


# Looping in a list
vowels = ["a", "e", "i", "o", "u"]
for each in vowels:
    print(each)  # a e i o u

# Looping in a tuple
vowels = ("a", "e", "i", "o", "u")
for each in vowels:
    print(each)  # a e i o u


# Looping in a string
data = "Hello World. I am learning python"
for each in data:
    print(each)  # H e l l o  W o r l d .  I a m  l e a r n i n g  p y t h o n


# Looping in a dictionary
student = {"name": "Raju", "email": "r@email.com", "address": "KTM"}

for each in student:
    print(each)  # name  email  address
