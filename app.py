import os

from flask import Flask, flash, url_for, redirect, request, render_template,request,session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import login_required

from db import (
    add_outlet,
    add_booking,
    add_invoice,
    add_invoice_item,
    add_invoice_payment,
    add_booking_payment,
    get_invoice_items,
    get_bookings,
    get_booking_balance,
    get_invoice_balance,
    get_invoices_for_outlet,
    get_unpaid_invoices,
    get_monthly_totals,
    get_monthly_payments   
)

#Configure application
app = Flask(__name__)

##dashboard & financial visibilty
