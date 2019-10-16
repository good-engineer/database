#userAcc.py

class UserAcc():
    ID=0
    name=""
    role=0
    conn=None

    def __int__(self, ID=0,name="",role=0,conn=None):
        self.ID = ID
        self.name = name
        self.role = role
        self.conn = conn

    def set_attrs(self,ID,name,role,conn):
        self.ID = ID
        self.name = name
        self.role = role
        self.conn = conn

#creat user account object 

user_acc = UserAcc()
