import math
from datetime import datetime


time = datetime.now()
DOTW = time.weekday()

subtotal = float(input("Please enter sub total:"))
tax = subtotal * .06
if (DOTW == 1 or DOTW == 2) and (subtotal >= 50):
    total = subtotal * 0.9 + tax
    discount = subtotal * 0.1
    print("Discount Amount: " + discount)
else:
    total = subtotal + tax
print("sales tax amount: " + str(round(tax, 2)))
print("total: " + str(round(total, 2)))