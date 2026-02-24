print("==============================")
print("------ STRING MANIPULATOR -----")
print()

#sentence input
sentence = input("Enter a sentence: ")

print("\n----- RESULTS -----")

# Original sentence
print("Original:", sentence)

# Total characters (with spaces)
with_space = len(sentence)
print("Characters (with spaces):", with_space)

# Total characters (without spaces)
without_space = len(sentence.replace(" ", ""))
print("Characters (without spaces):", without_space)

# Total words
words = sentence.split()
total_words = len(words)
print("Words:", total_words)

# UPPERCASE
print("UPPERCASE:", sentence.upper())

# lowercase
print("lowercase:", sentence.lower())

# Title Case
print("Title Case:", sentence.title())

# First word
if total_words > 0:
    print("First word:", words[0])
else:
    print("None")

# Last word
if total_words > 0:
    print("Last word:", words[-1])
else:
    print("None")

# Reversed sentence
reversed_sentence = sentence[::-1]
print("Reversed:", reversed_sentence)