print("==============================")
print("------ PRIME NUMBER CHECK -----")
print("==============================")

# Function to check if a number is prime
def prime(n):

    if n < 0:
        return "invalid number"

    if n == 0 or n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# -------- Part 1 --------
num = int(input("Enter a number: "))

result = prime(num)

if result == True:
    print(num, "is a PRIME number")

elif result == False:
    print(num, "is NOT a prime number")

else:
    print(result)

# -------- Part 2 --------
start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for number in range(start, end + 1):
    if prime(number) == True:
        print(number, end=", ")