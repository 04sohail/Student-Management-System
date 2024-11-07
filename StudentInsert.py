import oracledb as orc

# CREATING EXCEPTION CLASSES
class OnlyAphlabetsError(Exception): pass


class ZeroSizeError(Exception): pass

def ValidNameCheck(name):
    flag = False
    namelst = name.split()
    if len(namelst) == 0:
        raise ZeroSizeError
    for i in namelst:
        if not i.isalpha():
            flag = True
            break
    if flag:
        raise OnlyAphlabetsError
    else:
        return name


def InsertRecords():
    with open("SudentInfo.txt", "ab") as ab:
        try:
            print("-" * 50)
            srollno = int(input("Enter Student Roll Number : "))
            sname = ValidNameCheck(input("Enter Student Name : "))
            smark = float(input("Enter Student Marks : "))
            conn = orc.connect("system/root@localhost/xe")
            cur = conn.cursor()
            cur.execute("insert into studentsinfo values(:1, :2, :3)", (srollno, sname, smark))
            conn.commit()
            print("-" * 50)
            print("Your Data Is Successfully Inserted.")
            print("-" * 50)
            print()
        except ValueError:
            print("Don't Enter Alphabets, AlphaNumerics Or Special Symbols In The Place Of Student Roll Number And "
                  "Student Marks.")
        except OnlyAphlabetsError:
            print("!!! Enter Only Alphabets As Name.")
        except ZeroSizeError:
            print("You have not entered anything")
        except orc.DatabaseError as db:
            print("Database Error")
            print(db)
