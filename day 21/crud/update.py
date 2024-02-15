import json
filename="students.json"

def update_student():
    student_id=input("Enter student id")
    which_info=input("enter the info you want to change")
    new_info=input("Enter the new {which_info}")

    with open(filename,"r+")as fp:
        students=json.loads(fp.read())
        for student in students:
            if student[id]==id:
               student[which_info]=new_info
               break
            else:
                print("Invalid student id")
                want_to_continue=input("Do you want to continue?(y/n)")
                return True if want_to_continue.lower()=="y"else False
            fp.seek(0)
            fp.write(json.dumps(students,indent=2))

        print("Student Updated Successfully")
        want_to_continue=input("Do you want to continue?(y/n)")
        return True if want_to_continue.lower()=="y"else False



                

    import json
filename="day 21/crud/students.json"

def update_student():
    student_id=input("Enter student id")
    which_info=input("enter the info you want to change")
    new_info=input("Enter the new {which_info}")

    with open(filename,"r+")as fp:
        students=json.loads(fp.read())
        for student in students:
            if student[id]==id:
               student[which_info]=new_info
               break
            else:
                print("Invalid student id")
                want_to_continue=input("Do you want to continue?(y/n)")
                return True if want_to_continue.lower()=="y"else False
            fp.seek(0)
            fp.write(json.dumps(students,indent=2))

        print("Student Updated Successfully")
        want_to_continue=input("Do you want to continue?(y/n)")
        return True if want_to_continue.lower()=="y"else False
