--Database Schema

CREATE TABLE users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
)

CREATE TABLE outlets(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    outlet_name TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    contact_person_number TEXT NOT NULL
);

CREATE TABLE invoices(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    outlet_id INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
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
    invoice_id INTEGER,
    booking_id INTEGER,
    amount INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY(invoice_id) REFERENCES invoices(id),
    FOREIGN KEY(booking_id) REFERENCES bookings(id)
); 

CREATE TABLE bookings(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_number TEXT NOT NULL,
    booking_date TEXT NOT NULL,
    amount INTEGER NOT NULL,
    description TEXT NOT NULL
);
