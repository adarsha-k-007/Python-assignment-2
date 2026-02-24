print("============GRADE CALCULATOR===========")
print()
print("Enter the obtained Marks out of 100: ")
print()
marks = []
for i in range(1,6):
    n = int(input(f"Enter marks for subject {i} : "))
    marks.append(n)

total = sum(marks)
percentage = (total/500)*100

#grade
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
elif percentage < 50:
    grade = "F(fail)"  

#result
if all(n >= 40 for n in marks):
    result = "PASS"
else:
    result = "FAIL"

# output
print("\n__________MARKS DETAILS_________")
for i in range(5):
    print(f"Subject {i+1} : {marks[i]}")
# print("\nMarks    : ",marks)
print("--------------------------------")
print("Total      : ",total,"/500 ")
print("Percentage : ",percentage)
print("Grade      : ",grade)
print("Result     : ",result)
print("________________________________")