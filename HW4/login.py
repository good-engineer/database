#login.py

from userAcc import *
from DBconnection import *
from studentMenu import *
from instructorMenu import *

def login():
    
    print("welcome")

    while(user_acc.conn is None):

        print("please sign in")

        ID = input("%-10s:"%"ID")
        name = input("%-10s:"%"Name")

        auth(ID,name)

    switcher = {
            0 : student_menu.
            1 : instructor_menu
    }

    role_menu = switcher.get(user_acc.role)

    role_menu()

def auth(ID, name):

    user_connect = get_connect()

    #check if student exists

