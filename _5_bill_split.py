#user input:
bill = float(input("Total bill amount : "))
ppl = int(input("Number of people : "))
t = float(input("Tax percentage : "))
ti= float(input("Tip percentage : "))
print()
print("================================")
print("----    RESTAURANT BILL     ----")
print("================================")
print()
print("Sub Total :  $",bill)
print("People    : ",ppl)
#calculating tax percentage
tax = (t/100)*bill
print("Tax(%)    :  $",tax)
tax_total = bill+tax
#calculating tip percentage
tip = (ti/100)*tax_total
print("Tip(%)    :  $",tip)
print("--------------------------------")
#calculating total
total = tax_total+tip
print("Total     :  $",total)
print("--------------------------------")
#calculating per person amount
per = total/ppl
print("Per Person : $",per)
print("================================")