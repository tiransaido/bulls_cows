
import random

def generate_secret_number():
    return ''.join(random.sample('0123456789', 4))

def calculate_bulls_cows(secret, guess):
    bulls = 0
    cows = 0

    # Calculate bulls
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1

    # Calculate cows
    for digit in secret:
        if digit in guess:
            cows += 1

    cows -= bulls  # Remove the common bulls from cows count
    return bulls, cows


def main():
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to Bulls and Cows!")
    print("Try to guess the 4-digit number.")

    while True:
        guess = input("Enter your guess: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        attempts += 1
        bulls, cows = calculate_bulls_cows(secret_number, guess)

        if bulls == 4:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")

if __name__ == "__main__":
    main()
