num = int(input("How many numbers you want to add? : ")) #input
print()
numbers = []
for i in range(1,num+1):
    items = int(input(f"Enter the number {i} : "))
    numbers.append(items)  #adding into the list
    
print()
print("You gave: ",numbers)

total = sum(numbers)
print("\nSum of the Numbers : ",total)
print("Average of the Numbers : ",total/(len(numbers)))
print("Maximum Number : ",max(numbers))
print("Minimum Number : ",min(numbers))