--Database Schema

CREATE TABLE outlets(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    outlet_name TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    contact_person_number TEXT NOT NULL
);

CREATE TABLE invoices(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    outlet_id INTEGER NOT NULL,
    timestamp INTEGER NOT NULL,
    FOREIGN KEY(outlet_id) REFERENCES outlets(id)
);

CREATE TABLE invoice_item(
    item_id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    item_name TEXT NOT NULL,
    item_count INTEGER NOT NULL,
    unit_price INTEGER NOT NULL,
    line_total INTEGER NOT NULL,
    FOREIGN KEY(invoice_id) REFERENCES invoices(id)
);

CREATE TABLE payments(
    invoice_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    timestamp INTEGER NOT NULL,
    FOREIGN KEY(invoice_id) REFERENCES invoices(id)
); 

CREATE TABLE bookings(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_number TEXT NOT NULL,
    booking_date TEXT NOT NULL,
    booking_time TEXT,
    amount INTEGER NOT NULL,
)
