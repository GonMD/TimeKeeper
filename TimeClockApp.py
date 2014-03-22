import os
import sys
import sqlite3
import datetime

conn = sqlite3.connect('employeeDatabase.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY, name, dob)''')

answer = True
while answer:
    print("""
    Welcome to the Time Clock!
    1. Clock In
    2. Clock Out
    3. View Hours
    4. Add Employee
    5. List Employees
    6. Administrator
    7. Exit application
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

    elif answer == "4":
        nameFirst = input("\n Enter first name: ")
        nameMiddle = input("\n Enter middle name: ")
        nameLast = input("\n Enter last name: ")
        
        dateOfBirth = (input("\n Enter Date of Birth, eg. 4/22/1987: "))
        
        
        
        newEmployee = str(nameLast + ", " + nameFirst + " " + nameMiddle)

        c.execute("INSERT INTO users (name) VALUES ('" + newEmployee + "');" )
       
        conn.commit()

        

        print("\n New employee added: " + nameLast + ", " + nameFirst + " " + nameMiddle + ", born on " + dateOfBirth)
        
    elif answer == "5":
        print (newEmployee)

    elif answer == "6":
        print ("Test")

    
    elif answer == "7":
        sys.exit()

    else:
        print("\n Not a valid Choice. Please select an option.")
                    
