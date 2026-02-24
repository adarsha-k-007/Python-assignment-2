w = str(input("Enter WORD or NUMBER : "))
to_check = w.lower()                       #ignore case

if to_check[::+1] == to_check[::-1]:      #Checking palindrome
    result = "PALINDROME"
else:
    result = "NOT PALINDROME"

print("ORIGINAL SENTENCE : ",w)
print("REVERSED SENTENCE : ",w[::-1])           #Reversing
print("RESULT            : ",result)