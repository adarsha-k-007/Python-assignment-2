print("--------------Pattern Generaotr-------------")
print('--------------------------------------------')
print("Choose a Pattern:")
print("1. Increasing Numbers")
print("2. Repeating Numbers")
print("3. Reverse Decreasing")
print("4. Pyramid Pattern")
print("--------------------------------------------")
pat = int(input("Choose your pattern : "))
hei = int(input("Enter Height        : "))

if pat == 1:
    for i in range(1, hei + 1):                            # Pattern 1
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif pat == 2:
    for i in range(1, hei + 1):                            # Pattern 2
        for j in range(i):
            print(i, end=" ")
        print()

elif pat == 3:
    for i in range(hei, 0, -1):                            # Pattern 3
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

elif pat == 4:                                              # Pattern 4
    for i in range(1, hei + 1):
        for j in range(1, i + 1):                              
            print(j, end="")
        
        for j in range(i - 1, 0, -1):                           
            print(j, end="")
        print()

else:
    print("Invalid!")

print("--------------------------------------------")