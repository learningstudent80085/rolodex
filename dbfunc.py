import sqlite3

conn = sqlite3.connect("sample_db.db")

cursor = conn.cursor()

#cursor.execute("INSERT INTO contacts VALUES ('john','doe','123456789','john@doe.com');")
#conn.commit()
cursor.execute("SELECT rowid,* FROM contacts")
conn.commit()

data = cursor.fetchall()
for entry in data:
    print(entry)
conn.close()

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
    
    conn = sqlite3.connect("sample_db.db")
    cursor = conn.cursor()
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

#delete_entry()