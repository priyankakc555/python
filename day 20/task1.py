## Reading the binary file

import pickle
with open("output.dat", "rb") as fp:
    students = pickle.load(fp)

print(students) 
print(students[1]['name'])
print(students[1]['marks'])

