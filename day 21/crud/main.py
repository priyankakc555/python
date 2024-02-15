from create import create_student
from delete import delete_student
from update import update_student
from read import read_student
#import json/


def crud_student():
    selection=input("Enter your choice (c/r/u/d/e)")
    selection=selection.lower()
    def exit_message():
        print("thank you see you again !!!!")

    if selection =="c":
       cont= create_student()
       crud_student()if cont else exit_message()

    elif selection==("r"):
        read_student()
    elif selection==("u"):
        update_student()
    elif selection==("d"):
        delete_student()

    else:
        exit_message()


if __name__== '__main__':
    crud_student()

