#studentMenu.py

from userAcc import * 
from DBconnection import *

def student_menu():

    menu_num = -1

    while(menu_num != '0'):
        print("\n\nWelcome %s"%user_acc.name)
        print("select student menu\n")
        print("1) Student Report\n")
        print("2) View Time Table\n")
        print("3) Quit)\n")
        menu_num = input("Enter : ")

        switcher = {
                0 : quit_menu
                1 : print_stud_report,
                2 : print_time_table
        }

        selected_func = switcher.get(menu_num, print_wrong)

        selected_func()

    return


def print_stud_report():

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
