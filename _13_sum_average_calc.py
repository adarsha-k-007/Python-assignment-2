print("-----SUM AND AVERAGE CALCULATOR-----")
print()
num = int(input("How many numbers you want to add? : "))
print()

total = 0
maximum = None
minimum = None

for i in range(1, num+1):
    number = int(input(f"Enter the number {i} : "))

    total = total + number

    # For first number
    if i == 1:
        maximum = number
        minimum = number
    else:
        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

print()

print("Sum of the Numbers : ", total)
print("Average of the Numbers : ", total / num)
print("Maximum Number : ", maximum)
print("Minimum Number : ", minimum)
