print("==============================")
print("-------- TEXT ANALYSIS --------")
print("==============================")

# Count Words
def count_words(text):
    words = text.split()
    return len(words)

# Count Vowels
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count += 1
    return count

# Count Consonants
def count_consonants(text):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count

# Reverse Text
def reverse_text(text):
    return text[::-1]

# Check Palindrome
def palindrome(text):
    clean = text.lower().replace(" ", "")
    if clean == clean[::-1]:
        return True
    else:
        return False

# Remove Vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result

# Word Frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# Longest Word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Analyze Text (Main Function)
def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print("Longest word:", longest, "(", len(longest), "letters )")

    freq = word_frequency(text)
    print("Word Frequency:", end=" ")
    for key in freq:
        print(key + ":", freq[key], end=", ")
    print()


# Main Program
text = input("Enter text: ")
analyze_text(text)