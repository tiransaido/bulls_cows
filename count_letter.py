def count_letter_in_word(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

# Get input from the user
word = input("Enter a word: ")
letter = input("Enter a letter: ")
while True: 
    if len(letter) == 1:
        break 
    else:
         letter = input("Enter a letter with one char only: ")
# Call the function 
result = count_letter_in_word(word, letter)
# Display the result
print(f"The letter '{letter}' appears {result} times in the word '{word}'.")
