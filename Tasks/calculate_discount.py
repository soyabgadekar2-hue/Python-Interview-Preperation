def calculate_discount(amount):

    if amount >= 5000:
        discount_percentage = 20
    elif amount >= 300:
        discount_percentage = 10
    else:
        discount_percentage = 5

    discount_amount = amount * discount_percentage / 100
    final_amount = amount - discount_amount

    return discount_amount, final_amount


amount = float(input("Enter purchase amount: "))

discount, final_amount = calculate_discount(amount)

print("Discount amount:", discount)
print("Final payable amount:", final_amount)