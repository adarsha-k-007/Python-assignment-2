print("==========================")
print("---MOVIE TICKET BOOKING---")
print("--------------------------")
# user input
day = input("Enter Day : ").lower()
num = int(input("Number of Tickets : "))

base_price = 0

for i in range(1, num + 1):
    age = int(input(f"Enter your Age for ticket {i}: "))

    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 150
    elif 13 <= age <= 59:
        price = 300
    else:
        price = 200

    base_price += price  

# Day based discount
if day in ["monday", "tuesday", "wednesday", "thursday"]:
    discount = 0
else:
    discount = 0.20 * base_price

final_price = base_price - discount

print("-----------------------------")
print("Base Price           : ", base_price)
print("Discount             : ", discount)
print("Price after Discount : ", final_price)
print("-----------------------------")
print("Total Price          : ", final_price)