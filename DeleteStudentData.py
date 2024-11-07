import oracledb as orc
conn = orc.connect("system/root@localhost/xe")
cur = conn.cursor()
cur.execute("select * from studentinfo")
records = cur.fetchall()

def Delete():
    print("*"*50)
    delete = int(input("Enter Roll Number To Delete : "))
    print("*"*50)
    flag = False
    for record in records:
        # if record[0] == delete:
        #     flag = True
        print(record)
    # if flag:
    #     cur.execute("delete from studentinfo where sno = %d" % delete)
    #     print("*"*50)
    #     print("Record Deleted Successfully")
    #     print("*" * 50)
    # else:
    #     print("*" * 50)
    #     print("The Roll Number Doesn't Exist")
    #     print("*" * 50)