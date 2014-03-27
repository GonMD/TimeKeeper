import os
import sys
import sqlite3
import time
import re

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
    5. List Employees 
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

        #First name entry =======================================================

        while True:

            nameFirst = str(input("\n Enter first name: "))
            if re.match ("^[^A-Za-z]*$", nameFirst):
                print ("Use only letters.")

            else:
                break

        #Middle name entry =======================================================
                    
        while True:    
            
            nameMiddle = input("\n Enter middle name: ")
            if re.match ("^[^A-Za-z]*$", nameMiddle):
                print ("Use only letters.")

            else:
                break

        #Last name entry =======================================================

        while True:
            
            nameLast = input("\n Enter last name: ")
            if re.match ("^[^A-Za-z]*$", nameLast):
                print ("Use only letters.")

            else:
                break
        
        #Date of birth entry =======================================================

        while True:

            dateOfBirth = str(input("\n Enter Date of Birth, eg. XX/XX/XXXX: "))
            if re.match ("^\d{2}/\d{2}/\d{4}$", dateOfBirth):
                break

            else:
                print ("Use the supplied format")

        #Email entry =======================================================

        while True:

            emailAddress = str(input("\n Please enter your email address: "))
            if re.match ("^.+@.+$" , emailAddress):
                break

            else:
                print ("Use proper formatting")

        newEmployee = str(nameLast + ", " + nameFirst + " " + nameMiddle)

        c.execute('INSERT INTO users (name,dob,email) values(?,?,?)', (newEmployee, dateOfBirth, emailAddress))
        conn.commit()
        
        print("\n New employee added: " + nameLast + ", " + nameFirst + " " + nameMiddle + ", born on " + dateOfBirth)
        
    elif answer == "5":

        with conn:

            c.execute("SELECT * FROM users ")

            while True:

                row = c.fetchone()

                if row == None:
                    break

                print ("Employee ID [", row[0],"] |","Name:", row[1])

    elif answer == "6":

        

        answer = True
        while answer:
            print("""
            Administrator Sub Menu:
            1. Add Hours [TEST]
            2. Remove Hours [TEST]
            3. Remove Employee [TEST]
            4. Exit
         """)

            answer2 = input("Select an option.")

            if answer2 == "1":
                print ("Test 1")


            elif answer2 == "2":
                print ("Test 2")


            elif answer2 == "3":
                print ("Test 3")
                

            elif answer2 == "4":
                c.close()
                sys.exit()
                

            else:
                print ("\n Not a valid Choice. Please select an option.")
        
        elif answer == "7":
        c.close()
        sys.exit()

    else:
        print("\n Not a valid Choice. Please select an option.")
