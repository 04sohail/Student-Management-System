import oracledb as orc
# For One Student View
def SearchStudentDetails():
    try:
        conn = orc.connect("system/root@localhost/xe")
        cur = conn.cursor()
        cur.execute("select * from studentsinfo")
        records = cur.fetchall()
        sno = int(input("Enter Roll No Of Student To View The Data : "))
        flag = False
        for record in records:
            if record[0] == sno:
                flag = True
                break
        if flag:
            print("*" * 50)
            print("Data for Student Roll Number = {} Exists \nTo See The Data Go For \n'View Student Data Using "
                  "Roll Number'"
                  " In Main Menu".format(sno))
            print("*" * 50)
        else:
            print("*" * 50)
            print("Record Doesn't Exist.")
            print("*" * 50)

    except FileNotFoundError:
        print("File doesn't exist.")
    except orc.DatabaseError as db:
        print("Database Error")
        print(db)
