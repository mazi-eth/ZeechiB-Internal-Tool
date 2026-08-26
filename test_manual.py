from db import add_outlet, add_invoice, add_invoice_item, add_invoice_payment, get_invoice_balance, add_booking, add_booking_payment, get_booking_balance

# Set up test data
add_outlet("Test Outlet", "Jane Doe", "08000000000")
invoice_id = add_invoice("Test Outlet")
add_invoice_item(invoice_id, "7 inch cake", 5, 35000)
add_invoice_item(invoice_id, "11 inch cake", 10, 50000)
add_invoice_payment(invoice_id, 400000)

booking_id = add_booking("mazi", "0906523", "06-06-2026", 50000, "Its my Birthday")
add_booking_payment(booking_id, 25000)

booking_id2 = add_booking("AJManny", "081826", "26-08-2026", 100000, "Chert Anniversary")
add_booking_payment(booking_id2, 20000)



# Check the result
print("Balance:", get_invoice_balance(invoice_id))

print("Booking balance: ", get_booking_balance(booking_id))

print("Booking balance: ", get_booking_balance(booking_id2))
