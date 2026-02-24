print("==============================")
print("---- TEMPERATURE CONVERTER ----")
print("==============================")
print()

while True:
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    # Exit condition
    if choice == 7:
        print("Exited successfully")
        break

    # temperature input
    temp = float(input("Enter temperature value: "))

    # Celsius to Fahrenheit
    if choice == 1:
        result = (temp * 9/5) + 32
        print("Result:", result, "F")

    # Fahrenheit to Celsius
    elif choice == 2:
        result = (temp - 32) * 5/9
        print("Result:", result, "C")

    # Celsius to Kelvin
    elif choice == 3:
        result = temp + 273.15
        print("Result:", result, "K")

    # Kelvin to Celsius
    elif choice == 4:
        result = temp - 273.15
        print("Result:", result, "C")

    # Fahrenheit to Kelvin
    elif choice == 5:
        result = (temp - 32) * 5/9 + 273.15
        print("Result:", result, "K")

    # Kelvin to Fahrenheit
    elif choice == 6:
        result = (temp - 273.15) * 9/5 + 32
        print("Result:", result, "F")

    else:
        print("Please select between 1 to 7")

print()