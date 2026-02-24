print("==========-FACTORIAL CHECKER-==========")
print()
n = int(input("Enter the Number : "))
print()
# Handle negative numbers
if n < 0:
    print("Enter Positive numbers")

# Handle 0 case
elif n == 0:
    print("0! = 1")

else:

    fact = 1
    print(n,"! =", end=" ")
    for i in range(n, 0, -1):
        fact = fact * i
        print(i, end="")

        if i != 1:
            print(" x ", end="")

    print(" =", fact)