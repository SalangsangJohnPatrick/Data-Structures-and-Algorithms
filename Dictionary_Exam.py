#John Patrick M. Salangsang CS - 201

DICT_EXAM = {"Code":1212,
             "Product":"Cream",
             "Amount":125,
             "Quantity":10}

with open("Salangsang_ODD_Prob2.txt", "w+") as f:
    x = DICT_EXAM.get("Amount")
    y = DICT_EXAM.get("Quantity")
    total = x * y
    discount = total * .10
    totalAmtPay = total - discount
    f.write(f"Code: {DICT_EXAM.get('Code')}\n")
    f.write(f"Product: {DICT_EXAM.get('Product')}\n")
    f.write(f"Amount: {DICT_EXAM.get('Amount')}\n")
    f.write(f"Quantity: {DICT_EXAM.get('Quantity')}\n")
    f.write(f"Total: {total}\n")
    f.write("Discount: {:.0f}\n".format(discount))
    f.write("Total Amount to be pay: {:.0f}\n".format(totalAmtPay))
f.close()
