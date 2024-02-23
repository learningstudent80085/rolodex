import sqlite3

def add_entry():
    first = input("Enter first name \n")
    last = input("Enter last name \n")
    phone = input("Enter phone number \n")
    email = input("Enter email \n")
    conn = sqlite3.connect("sample_db.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)", (first,last,phone,email))
    conn.commit()
    conn.close()

def search_entry():
    first = input("Enter first name")
    last = input("Enter last name")
    conn = sqlite3.connect("sample_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid,* FROM contacts WHERE first LIKE $?$ OR last LIKE $?$",(first,last))
    conn.commit()
    data = cursor.fetchall()
    for entry in data:
        print(entry)
    conn.close()

def update_entry():
    idnum = input("Enter ID number \n")
    first = input("Enter first name \n")
    last = input("Enter last name \n")
    phone = input("Enter phone number \n")
    email = input("Enter email \n")
    conn = sqlite3.connect("sample_db.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET first=?, last=?, phone=?, email=? WHERE rowid=?",(first,last,phone,email,idnum))
    conn.commit()
    conn.close()

def delete_entry():
    idnum = input("Enter ID number")
    conn = sqlite3.connect("sample_db.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE rowid=?",(idnum))
    conn.commit()
    conn.close()
    print("entry deleted")
