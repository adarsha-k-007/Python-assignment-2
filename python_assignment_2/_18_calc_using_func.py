print("===========================")
print("-------- CALCULATOR --------")
print("===========================")

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Modulus
def modulus(a, b):
    if b == 0:
        return "Cannot perform modulus by zero"
    return a % b

# Power
def power(a, b):
    return a ** b

# Main Calculator Menu
def calculator():

    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            print("Exiting Calculator...")
            break

        if choice >= 1 and choice <= 6:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(a, b))

            elif choice == 2:
                print("Result:", subtract(a, b))

            elif choice == 3:
                print("Result:", multiply(a, b))

            elif choice == 4:
                print("Result:", divide(a, b))

            elif choice == 5:
                print("Result:", modulus(a, b))

            elif choice == 6:
                print("Result:", power(a, b))

        else:
            print("Invalid choice! Please select 1-7.")
# Calling main function
calculator()