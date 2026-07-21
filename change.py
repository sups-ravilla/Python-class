def calculate_due_amount(total_bill, amount_paid):

    change_due = amount_paid - total_bill

    return change_due

bill_amount = 2.50

paid_amount = 4.00

returned_change = calculate_due_amount(bill_amount, paid_amount)

print(f"Total Bill: ${bill_amount:.2f}")
print(f"Amount Paid: ${paid_amount:.2f}")
print(f"Shopkeeper should return: ${returned_change:.2f}")
