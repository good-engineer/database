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
    
    c = user_connect.cursor()
    c.execute("SELECT * FROM student\
            WHERE ID=\"%s\" and name=\"%s\""%(ID,name))
    data = c.fetchone()
    if data is not None
       user_acc.set_attrs(ID,name,0,user_connect)
       return
   else
       c.execute("SELECT * FROM instructor\
               WHERE ID=\"%s\" and name=\"%s\""%(ID,name))
       data = c.fetchone()
       if data is not None
           user_acc.set_attrs(ID,name,1,user_connect)
           return
       else
           print("Your ID and name is not valid!")
           return_connect(user_connect)
           return
