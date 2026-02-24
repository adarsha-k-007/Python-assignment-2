print("=======================")
year = int(input("\nEnter the Year : "))     #input

if year%4 == 0 and year%100 !=0 or year%400 ==0:            # should satisfy by all 3 conditions
    res = "LEAP YEAR"
else :
    res = "NOT LEAP YEAR"

print("===================")
print(res)
print("===================\n")