
year = int(input("Enter your Birth Year: "))
#using inbuilt library:
# from datetime import date
# cur_yr = date.today().year
# age = cur_yr-year

# without importing library:
age = 2026-year

print("---------------------")
print("YOUR AGE DETAILS:")
print("---------------------")
print(" Current Age: ",age)
print(" Age in months: ",age*12)
print(" Age in days: ",age*365)
print(" Age in hours: ",age*365*24)
print(" Age in minutes: ",age*365*24*60)
print(" Years until age 100: ",100-age)