import random

print("==============================")
print("------ NUMBER GUESS GAME ------")
print("==============================")

def play_game(best_score):                  # Function to play one game
                                                    
    ran = random.randint(1, 100)
    attempts = 7
    used_attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("You have 7 attempts t guess that!")

    while attempts > 0:

        guess = int(input("Enter your guess: "))
        used_attempts += 1
        attempts -= 1

        if guess == ran:
            print("Correct! You guessed it.")
            print("Attempts used:", used_attempts)

            if best_score is None or used_attempts < best_score:          # Update best score
                best_score = used_attempts
                print("New Best Score:", best_score)

            return best_score

        elif guess > ran:
            print("Too High!")

        else:
            print("Too Low!")

        if abs(guess - ran) <= 5:                                 # Bonus hint (within 5)
            print("You are very close!")

        print("Attempts remaining:", attempts)

    print("You lost! The number was:", ran)                    # If failed

    return best_score

def main():                                # Main program

    best_score = None

    while True:
        best_score = play_game(best_score)

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing!")
            break

main()                        # Run program