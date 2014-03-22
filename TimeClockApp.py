import os
import sys
import sqlalchemy.0.9.3
import pickle
import datetime


answer = True
while answer:
    print("""
    Welcome to the Time Clock!
    1. Clock In
    2. Clock Out
    3. View Hours
    4. Add Employee
    5. List Employees
    6. Exit application
""")

    answer = input("Select an option.")

    if answer == "1":
        employeeId = input("Enter employee ID number: ")
        timeStamp = str(datetime.datetime.now())
        print(employeeId + "\n Clocked in at " + timeStamp)

    elif answer == "2":
        employeeId = input("Enter employee ID number: ")
        timeStamp = str(datetime.datetime.now())
        print("\n Clocked out at " + timeStamp)

    elif answer == "3":
        print("\n Hours: X")
        os.system('CLS')

    elif answer == "4":
        nameFirst = input("\n Enter first name: ")
        nameMiddle = input("\n Enter middle name: ")
        nameLast = input("\n Enter last name: ")
        dateOfBirth = input("\n Enter Date of Birth, eg. 4/22/1987: ")
        newEmployee = str(nameLast + ", " + nameFirst + " " + nameMiddle)

        employeeDatabase = { newEmployee }

        #pickle.dump( employeeDatabase, open("employeeDatabase.p", "wb") )

        print("\n New employee added: " + nameLast + ", " + nameFirst + " " + nameMiddle + ", born on " + dateOfBirth)
        
    elif answer == "5":
        print (newEmployee)


    elif answer == "6":
        sys.exit()

    else:
        print("\n Not a valid Choice. Please select an option.")
                    
