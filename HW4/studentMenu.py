#studentMenu.py

from userAcc import * 
from DBconnection import *

def student_menu():

    menu_num = ''

    while(menu_num != '0'):
        print("\n\nWelcome %s"%user_acc.name)
        print("select student menu")
        print("1) Student Report")
        print("2) View Time Table")
        print("3) Quit)")
        menu_num = input("Enter : ")

        switcher = {
                '0' : quit_menu,
                '1' : print_stud_report,
                '2' : print_time_table
        }

        selected_func = switcher.get(menu_num, print_wrong)

        selected_func()

    return


def print_stud_report():

    c = user_acc.conn.cursor()
    c.execute("SELECT * FROM student \
               WHERE ID = {} and name = {}".format(user_acc.ID, user_acc.name))
    
    data = c.fetchone()

    print("You are a member of {}".format(data[2]))
    print("You have taken total {} credits\n".format(data[3]))
    print("Semester report\n")

    return

def print_time_table():

    return

def quit_menu():

    return

def gp_to_float(grade):

    return

def selected_func(menu_num,print_wrong):

    return

def print_wrong():

    return
