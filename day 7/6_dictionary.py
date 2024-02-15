# min()
# It also takes iterable as an input and returns the minimum from that iterable
print(min(4, 5, 1, 8, 10))  # 1


# sorted()
# It also takes iterable and returns the sorted data

data = sorted([7, 1, 3, 2, 10, 15])
print(list(data))

data = sorted([7, 1, 3, 2, 10, 15], reverse=True)
print(list(data))  # [15, 10, 7, 3, 2, 1]


# reversed()
# It also takes iterable and returns the reversed data

data = reversed([7, 1, 3, 2, 10, 15])
print(list(data))  # [15, 10, 2, 3, 1, 7]

name = student.get("name")
age = student.get("age")
roll = student.get("roll")   # None