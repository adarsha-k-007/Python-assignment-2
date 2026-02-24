print("==============================")
print("------ NUMBER FUNCTIONS -------")
print("==============================")

# Factorial
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

# Prime Check
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Fibonacci (nth term)
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        return b

# Sum of Digits
def sum_of_digits(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n = n // 10
    return total

# Reverse Number
def reverse_number(n):
    rev = 0
    n = abs(n)
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    return rev

# Armstrong Number
def armstrong(n):
    temp = n
    power = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp = temp // 10

    return total == n

# GCD
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Perfect Number
def perfect_number(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

# Menu
def menu():
    while True:
        print("\n1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif choice == 2:
            n = int(input("Enter number: "))
            print("Prime:", prime(n))

        elif choice == 3:
            n = int(input("Enter term number: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == 4:
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == 5:
            n = int(input("Enter number: "))
            print("Reversed:", reverse_number(n))

        elif choice == 6:
            n = int(input("Enter number: "))
            print("Armstrong:", armstrong(n))

        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == 9:
            n = int(input("Enter number: "))
            print("Perfect Number:", perfect_number(n))

        elif choice == 10:
            print("Exiting Program...")
            break

        else:
            print("Invalid choice!")

menu()                  # Call Menu