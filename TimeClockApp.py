import os
import sys
import sqlite3
import time

conn = sqlite3.connect('employeeDatabase.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY, name TEXT, dob INTEGER, email TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS logs(
    id INTEGER PRIMARY KEY, employeeId INTEGER, checkInDate INTEGER, checkInTime INTEGER, checkOutTime INTEGER)''')

answer = True
while answer:
    print("""
    Welcome to the Time Clock!
    1. Clock In
    2. Clock Out
    3. View Hours [TEST]
    4. Add Employee
    5. List Employees [TEST]
    6. Administrator [TEST]
    7. Exit application
""")

    answer = input("Select an option.")

    if answer == "1":
        employeeId = input("Enter employee ID number: ")
        dateStamp = str(time.strftime("%d/%m/%Y"))
        
        timeStamp = str(time.strftime("%I:%M:%S"))
        print(employeeId + "\n Clocked in at " + timeStamp)

        c.execute('INSERT INTO logs (employeeId, checkInDate, checkInTime) values (?,?,?)', (employeeId , dateStamp, timeStamp))
        conn.commit()

    elif answer == "2":
        employeeId = input("Enter employee ID number: ")
        dateStamp = str(time.strftime("%d/%m/%Y"))
        timeStamp = str(time.strftime("%I:%M:%S"))

        c.execute('SELECT * FROM logs ORDER BY checkOutTime LIMIT 1')
        fetchRowId = c.fetchone()
        rowId = fetchRowId[0]
        
        
        print("\n Clocked out at " + timeStamp)
        
        c.execute('UPDATE logs SET checkOutTime=? WHERE Id=? ', (timeStamp , rowId))
        conn.commit()

    elif answer == "3":
        print("\n Hours: X")

    elif answer == "4":
        nameFirst = input("\n Enter first name: ")
        nameMiddle = input("\n Enter middle name: ")
        nameLast = input("\n Enter last name: ")
        dateOfBirth = str(input("\n Enter Date of Birth, eg. 4/22/1987: "))
        emailAddress = str(input("\n Please enter your email address: "))

        newEmployee = str(nameLast + ", " + nameFirst + " " + nameMiddle)

        c.execute('INSERT INTO users (name,dob,email) values(?,?,?)', (newEmployee, dateOfBirth, emailAddress))
        conn.commit()
        
        print("\n New employee added: " + nameLast + ", " + nameFirst + " " + nameMiddle + ", born on " + dateOfBirth)
        
    elif answer == "5":
        print (newEmployee)

    elif answer == "6":
        print ("Test")

    
    elif answer == "7":
        c.close()
        sys.exit()

    else:
        print("\n Not a valid Choice. Please select an option.")
                    
