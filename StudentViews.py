import pickle

import oracledb as orc

conn = orc.connect("system/root@localhost/xe")
cur = conn.cursor()


# For One Student View
def StudentView():
    sno = int(input("Enter Roll No Of Student To View The Data : "))
    cur.execute("select * from studentsinfo where sno = %d" % sno)
    colnames = cur.description
    record = cur.fetchone()
    if record != None:
        print("*" * 50)
        for val in colnames:
            print("\t", val[0], end="\t")
        print()
        print("*" * 50)
        for val in record:
            print("\t", val, end="\t\t")
        print()
        print("*" * 50)
    else:
        print("*" * 50)
        for val in colnames:
            print("\t", val[0], end="\t")
        print()
        print("*" * 50)
        print("Sorry No Record For Roll Number %d" % sno)
        print("*" * 50)


# For All Student View
def StudentViews():
    cur.execute("select * from studentsinfo")
    colnames = cur.description
    allrecords = cur.fetchall()
    print("*" * 50)
    for val in colnames:
        print("\t", val[0], end="\t")
    print()
    print("*" * 50)
    for record in allrecords:
        for val in record:
            print("\t", val, end="\t\t")
        print()
