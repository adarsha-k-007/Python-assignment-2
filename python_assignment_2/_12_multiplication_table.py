print("-----TABLES-----")

num = int(input("\nEnter the number : "))
ran = int(input("Enter the Range  : "))

for i in range(1,ran+1):
    print(num ,"x", i, "=", num*i)              # printing in table form

print("-----------------")

#Bonus
print("\n-----FULL TABLE (1-10)-----")

for i in range(1, 11):      # This is multiplier (1 to 10)
    for j in range(1, 11):  # This is table number (1 to 10)
        print(j, "x", i, "=", j*i, end="     ")  

    print()   # move to next row

print("----------------------------------------")