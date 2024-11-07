from StudentMenu import menu
from StudentInsert import InsertRecords
from StudentViews import StudentView, StudentViews
from StudentSearch import SearchStudentDetails
from DeleteStudentData import Delete
while True:
    menu()
    try:
        ch = int(input("Enter Your Choice : "))
        match ch:
            case 1:
                InsertRecords()
            case 2:
                StudentView()
            case 3:
                StudentViews()
            case 4:
                SearchStudentDetails()
            case 5:
                Delete()
            case 6:
                print("Thanks For Using This Program.")
                break
            case _:
                print("Your Selection Of Operation Is Wrong. Try Again !!!")
    except ValueError:
        print("Don't Enter Alphabets, Alphanumeric Or Special Symbols.Enter Numericals Only. Try Again !!!")
