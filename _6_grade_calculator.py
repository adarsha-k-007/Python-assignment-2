print("============GRADE CALCULATOR===========")
print()
print("Enter the obtained Marks out of 100: ")
print()

total = 0
pas = True   # To check all subjects >= 40

# Taking marks input
for i in range(1, 6):
    n = int(input(f"Enter marks for subject {i} : "))

    total = total + n

    if n < 40:
        pas = False

percentage = (total / 500) * 100


# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F (Fail)"


# Result Calculation
if pas:
    result = "PASS"
else:
    result = "FAIL"


# Output
print("\n__________MARKS DETAILS_________")
print("--------------------------------")
print("Total      : ", total, "/500")
print("Percentage : ", percentage)
print("Grade      : ", grade)
print("Result     : ", result)
print("________________________________")
