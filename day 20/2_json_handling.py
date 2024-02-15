#JSON stands for javascript object notation
#it is a file format to store data so that it could be rendered and parsed easily
#it vlooks similar to the python dictionary
#they are mostly used to share information among different entities(fronted and backend,mobile and backend,backend and backend)
#python has a built-in json module

import json
filename="day20/student.json"

student={"name":"Alex","age":20,"address":"KTM"}

with open(filename,"w")as fp:
    data=json.dumps(student)
    fp.write(data)


    with open(filename,"r")as fp:
        student=fp.read()
        student=json.loads(student)

        print(student)
        print(student["age"])
        print(type(student))
        