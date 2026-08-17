import sqlite3


#open a database connection
def connect_db():
    conn = sqlite3.connect("zeechib.db")
    return conn 

#add an outlet

def add_outlet(name, contact_person, contact_number):
    conn = connect_db()

    #Database cursor object for executing SQL.
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO outlets (outlet_name, contact_person, contact_person_number) VALUES (? ,?, ?)", (name, contact_person, contact_number)
    )
    conn.commit()
    conn.close()
