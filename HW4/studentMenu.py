#studentMenu.py

from userAcc import * 
from DBconnection import *
from functools import cmp_to_key

def student_menu():

    menu_num = -1

    while(menu_num != '0'):
        print("Please select student menu")
        print("1) Student Report")
        print("2) View Time Table")
        print("0) Exit")
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
    c.execute('SELECT * FROM student WHERE ID=%s and name="%s"'%(user_acc.ID, user_acc.name))
    data = c.fetchone()

    print("Welcome %s"%data[1])
    print("You are a member of %s"%data[2])
    print("You have taken total %s credits\n"%data[3])
    print("Semester report\n")

    def compareSemester(lhs, rhs):
        if lhs[0] > rhs[0]:
            return 1
        elif lhs[0] < rhs[0]:
            return -1
        else:
            if lhs[1] == 'Winter':
                return 1
            if lhs[1] == 'Fall':
                if rhs[1] == 'Winter':
                    return -1
                return 1
            if lhs[1] == 'Summer':
                if rhs[1] == 'Spring':
                    return 1
                return -1
            if lhs[1] == 'Spring':
                return -1



    #finding grades and credits
    c.execute(f'SELECT DISTINCT year, semester FROM takes WHERE  ID={user_acc.ID}')

    takes = c.fetchall()
    takesList = sorted(takes, key=cmp_to_key(compareSemester), reverse=True)

    for takes in takesList:
        c.execute(f'SELECT credits, grade, course_id, title, dept_name FROM takes NATURAL JOIN course WHERE takes.ID={user_acc.ID} and year={takes[0]} and semester="{takes[1]}"')


        something = c.fetchall()
        sumOfCredits = 0
        sumOfGrades = 0.0


        flag = 0
        for cg in something:
            sumOfCredits += cg[0]

            if cg[1] is None:
                sumOfGrades += 0
            else:
                flag = 1
                sumOfGrades += float(cg[0]) * gp_to_float(cg[1])

        if flag == 0:
            print("%s\t%s\tGPA : %s"%(takes[0], takes[1], None))
        else:
            print("%s\t%s\tGPA : %f"%(takes[0], takes[1], sumOfGrades/float(sumOfCredits)))

        print("%10s\t%40s\t%15s\t%8s\t%8s"\
              %("course_id", "title", "dept_name", "credit", "grade"))

        # print info
        for cg in something:
            cid = cg[2]
            t = cg[3]
            d = cg[4]
            cr = cg[0]
            g = cg[1]
            print("%10s\t%40s\t%15s\t%8s\t%8s"%(cid, t, d, cr, g))

    c.close()

    return


def print_time_table():
    c = user_acc.conn.cursor()


    print("\nTime Table\n")
    print("%10s\t%40s\t%15s\t%10s\t%10s"%("course_id", "title", "day", "start_time", "end_time"))

    #make time table with most recent year, semester of user






    c.close()

    return


def quit_menu():
    global user_acc

    return_connect(user_acc.conn)

    del user_acc

    return

def gp_to_float(grade):
    return {
        "A+": 4.3,
        "A": 4,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1,
        "D-": 0.7,
        "F": 0
    }[grade]


def print_wrong():
    print("\nwrong menu number.")
    return