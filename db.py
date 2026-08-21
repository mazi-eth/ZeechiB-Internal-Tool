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

#add_invoice, return invoice ID
def add_invoice(outlet_name):
    conn = connect_db()

    cursor = conn.cursor()

    outlet_id = cursor.execute(
        "SELECT id FROM outlets WHERE outlet_name = ?", (outlet_name,)
    ).fetchone()

    if outlet_id is None:
        return None
    #return the item in the tuple
    outlet_id = outlet_id [0]
    cursor.execute(
        "INSERT INTO invoices (outlet_id, timestamp) VALUES (?, date('now'))", (outlet_id,)
    )
    conn.commit()
    invoice_id = cursor.lastrowid
    conn.close()
    return invoice_id

#add_invoice_item(invoice ID, item name, count, unit_price)
def add_invoice_item(invoice_id, item_name, item_count, unit_price):
    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO invoice_item (invoice_id, item_name, item_count, unit_price, line_total) VALUES (?, ?, ?, ?, ?)", (invoice_id, item_name,  item_count, unit_price, (item_count * unit_price))
    )
    conn.commit()
    conn.close()

#add_payment(invoice ID, amount, timestamp)
def add_payment(invoice_id, amount):
    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO payments (invoice_id, amount, timestamp) VALUES (?, ?, date('now'))", (invoice_id, amount)
    )
    conn.commit()
    conn.close()

#get_invoice_items(invoice_id)
def get_invoice_items(invoice_id):
    conn = connect_db()
    cursor = conn.cursor()

    invoice_rows = cursor.execute (
        "SELECT item_name, item_count, unit_price, line_total FROM invoice_item WHERE invoice_id = ?", (invoice_id, )
    ).fetchall()

    #route call will do the unwrapping

    conn.close()

    return invoice_rows

    

    

#get_invoice_balance(invoice_id)
def get_invoice_balance(invoice_id):
    conn = connect_db()
    cursor = conn.cursor()

    total_invoiced = cursor.execute (
        "SELECT SUM(line_total) FROM invoice_item WHERE invoice_id = ?", (invoice_id, )
    ).fetchone()
    total_invoiced = total_invoiced[0]

    total_payment = cursor.execute (
        "SELECT SUM(amount) FROM payments WHERE invoice_id = ?", (invoice_id, )
    ).fetchone()
    total_payment = total_payment [0]

    conn.close()

    if total_invoiced is None:
        total_invoiced = 0
    if total_payment is None:
        total_payment = 0
    balance = total_invoiced - total_payment
    return balance
      

#get_invoices_for_outlet(outlet_name)
  






#get_unpaid_invoices

#get_monthly_totals(month, year)
