from db import add_outlet, add_invoice, add_invoice_item, add_payment, get_invoice_balance

# Set up test data
add_outlet("Test Outlet", "Jane Doe", "08000000000")
invoice_id = add_invoice("Test Outlet")
add_invoice_item(invoice_id, "7 inch cake", 5, 35000)
add_invoice_item(invoice_id, "11 inch cake", 10, 50000)
add_payment(invoice_id, 400000)

# Check the result
print("Balance:", get_invoice_balance(invoice_id))
