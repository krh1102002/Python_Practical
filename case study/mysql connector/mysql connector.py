import mysql.connector
from datetime import date
from tabulate import tabulate

def displayALl():
    cur.execute("SELECT * FROM STUDENT_RECORD")
    alldata = cur.fetchall()
    fields = []
    cur.execute("desc STUDENT_RECORD")
    cols = cur.fetchall()
    for i in cols:
        fields.append(i[0])
    print(tabulate(alldata, headers=fields))

def dispNameAge():
    cur.execute("SELECT FIRST_NAME,MIDDLE_NAME,LAST_NAME,DOB FROM STUDENT_RECORD")
    data = cur.fetchall()
    today = date.today()
    x = []
    for i in data:
        age = today - i[-1]
        x.append((i[0] + " " + i[1] + " " + i[2], age.days // 365))
    print(tabulate(x, headers=["NAME", "AGE"]))

def addRecord():
    print("...Adding new record...")
    prn = input("Enter the PRN number: ")
    f_n = input("Enter First name: ").upper()
    m_n = input("Enter Middle name: ").upper()
    l_n = input("Enter Last name: ").upper()
    ad = input("Enter Address: ").upper()
    ph = input("Enter phone number: ")
    em = input("Enter email id: ").lower()
    dt = input("Enter date of birth(yyyy-mm-dd): ")

    insert = "INSERT INTO STUDENT_RECORD VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(prn, f_n, m_n, l_n, ad, ph,
                                                                                           em, dt)
    cur.execute(insert)
    mycon.commit()
    print("Record added SUCCESSFULLY")

def delRecord():
    prn = input("Enter the PRN whose record is to be deleted: ")
    query = "DELETE FROM STUDENT_RECORD WHERE PRN='{}'".format(prn)
    cur.execute(query)
    mycon.commit()
    print("Record DELETED Successfully")

def updatePhoneEmail():
    prn = input("Enter the PRN whose record is to be updated: ")
    mob = input("Enter new mobile number: ")
    em = input("Enter new email id: ")
    query = "UPDATE STUDENT_RECORD SET MOBILE_no='{}',EMAIL_id='{}' WHERE PRN='{}'".format(mob, em, prn)
    cur.execute(query)
    mycon.commit()
    print("Database updated Successfully")

def addCGPA(flag):
    if flag:
        query = "ALTER TABLE STUDENT_RECORD ADD COLUMN CGPA FLOAT"
        cur.execute(query)
        mycon.commit()
        print("\n CGPA field added successfully...\n")
        cur.execute("SELECT PRN FROM STUDENT_RECORD")
        x = cur.fetchall()
        for i in x:
            prn = i[0]
            print("Enter the CGPA of PRN ", prn, end=': ')
            cgpa = float(input())
            query = "UPDATE STUDENT_RECORD SET CGPA='{}' WHERE PRN='{}'".format(cgpa, prn)
            cur.execute(query)
            mycon.commit()
        return False
    else:
        print("The field CGPA already exists.")
        return True

def functions():
    print('''
            1. Display the database
            2. Display name and age of all students
            3. Add record 
            4. Delete a record
            5. Update email and Phone number
            6. Add column CGPA

            Enter any other key to exit

    ''')

if __name__ == "__main__":
    print(" "*65,"Welcome")
    print("--" * 72)
    mycon = mysql.connector.connect(host="localhost", user="hulke1102002", password="hulke@123", database="kunal")
    cur = mycon.cursor()
    global flag
    flag = False
    try:
        cur.execute("ALTER TABLE STUDENT_RECORD DROP COLUMN CGPA")
    except:
        pass
    flag = True
    if mycon.is_connected():
        functions()
        while True:
            opt = input("Select your choice(h for help): ")
            if opt == '1':
                displayALl()
            elif opt == '2':
                dispNameAge()
            elif opt == '3':
                addRecord()
            elif opt == '4':
                delRecord()
            elif opt == '5':
                updatePhoneEmail()
            elif opt == '6':
                flag = addCGPA(flag)
            elif opt in 'hH':
                functions()
            else:
                break
    else:
        print("Unable to connect to MySQL")