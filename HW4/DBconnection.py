#DBconnection

import MySQLdb

db_host = "localhost"
db_user = "root"
db_pw = " "
db_name = "pyhton_testdb"

connect_pool = []

def connectDB():
    connect = MySQLdb.connect(host=db_host, user=db_user,
                              password=db_pw, database=db_name)
    return connect

def get_connect():
    global connect_pool
    if not connect_pool:
        connect_tmp = connectDB()
        connect_pool.append(connect_tmp)
    return connect_pool.pop()

def return_connect(conn):
    global connect_pool
    connect_pool.append(conn)
    return

def lose_db(db):
    db.close()
    return
