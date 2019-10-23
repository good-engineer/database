#instructorMenu.py

from userAcc import *

def instructor_menu():

    menu_num = ''

    while(menu_num != '0'):
        print("\n\nWelcome %s"%user_acc.name)
        print("Please select instructor menu")
        print("1) Course report")
        print("2) Advisee report")
        print("0) Quit")
        menu_num = input("Enter : ")

        switcher = {
                '0' : quit_menu,
                '1' : print_course_report,
                '2' : print_advisee_report
        }

        selected_func = switcher.get(menu_num, print_wrong)

        selected_func()
    
    return

def print_course_report(c):

    # c = user_acc.conn.cursor()
    # c.execute("SELECT max(year) FROM teaches \
    #            WHERE ID = {} and name = {}".format(user_acc.ID, user_acc.name))
    c.execute("select max(year) from teaches")

    recent_year = c.fetchone()[0]

    c.execute("select * from teaches \
               where year = {}".format(recent_year))
    
    teaches = c.fetchall()

    recent_semester = 'Spring'
    for item in teaches:
        if 'Summer' in item:
            recent_semester = 'Summer'
    for item in teaches:
        if 'Fall' in item:
            recent_semester = 'Fall'
    for item in teaches:
        if 'Winter' in item:
            recent_semester = 'Winter'

    teaches = [x for x in teaches if x[3]==recent_semester]

    print("Course report - {} {}".format(recent_year, recent_semester))

    for t in teaches:
        c.execute("select * from section natural join course \
                   where course_id = {} and sec_id = {}".format(t[1], t[2]))
        a = c.fetchone()

        c.execute("select * from time_slot \
                   where time_slot_id = {}".format(a[6]))
        times = c.fetchall()
        time_str = ''
        for i, time in enumerate(times):
            time_str += time[1]
            if i + 1 != len(times):
                time_str += ', '
            else:
                time_str += str(time[2]) + ' : ' + str(time[3]) + ' - ' + str(time[4]) \
                            + ' : ' + str(time[5])

        print("{:8}{}      [{} {}] ({}, {})".format(a[0], a[7], a[4], a[5], a[6], time_str))
        print("ID      name    dept_name       grade")

        c.execute("select * from takes natural join student \
                   where course_id = {} and sec_id = {} and \
                   semester = {} and year = {}".format(t[1],t[2],t[3],t[4]))
        students = c.fetchall()

        for student in students:
            print("{:8}{:8}{:16}{}".format(student[0],student[6],student[7],student[5]))

        print("")

    return

def print_advisee_report():

    return

def quit_menu():

    return

def print_wrong():
    
    print("\nWrong menu number!")

    return
