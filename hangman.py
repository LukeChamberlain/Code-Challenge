import random

print(f"Welcome to Hangman!\n")
def main():
    words =  ["code", "file", "selection", "view", "terminal", "challenge", "chrome", "british", "football", "cougars"]
    word_of_choice = random.choice(words)

    def word_to_underscores(word_of_choice):
        letters = ""
        letters += "_"*len(word_of_choice)
        return letters

    word_in_underscores = word_to_underscores(word_of_choice)

    print(f"{word_in_underscores} <-- (You have {len(word_of_choice)} letters remaining)")
    print(word_of_choice)

    letters_lst = list(word_of_choice)
    underscores_lst = list(word_in_underscores)
    letter_guessed_lst = []

    def guess(letters_lst, underscores_lst):
        num_of_guesses_total = 0
        num_of_correct_guesses = 0
        num_of_incorrect_guesses = 0
        while "_" in underscores_lst:
            letter_guessed = input("Please Guess a Letter: ").lower()
            if letter_guessed in letters_lst:
                num_of_guesses_total += 1
                num_of_correct_guesses += 1
                for index, char in enumerate(letters_lst):
                    if char == letter_guessed:
                        underscores_lst[index] = letter_guessed
                word_in_underscores = "".join(underscores_lst)
                print(f"{word_in_underscores} <-- (You have {len(word_of_choice) - num_of_correct_guesses} letters remaining)")
            else:
                num_of_guesses_total += 1
                num_of_incorrect_guesses += 1
                print("Sorry that letter is not in the word.")
                print(f"{word_in_underscores} <-- (You have {len(word_of_choice) - num_of_correct_guesses} letters remaining)")
                letter_guessed_lst.append(letter_guessed)
            print(*letter_guessed_lst, sep = ", ") 
            print(f"You have made {num_of_guesses_total} total guesses, {num_of_correct_guesses} correct guesses, {num_of_incorrect_guesses} incorrect guesses")
        print(f"You guessed the word correctly, with a total of {num_of_guesses_total} guesses.")
    guess(letters_lst, underscores_lst)

main()

def keep_playing():
    quit_or_continue = input(f"\nWould you like to keep playing Yes or Quit: ").lower()
    if quit_or_continue == "yes":
        main()
    elif quit_or_continue == "quit":
        return
    else:
        print(f"\nThat is not a valid response please try again.")
        keep_playing()
        
keep_playing()

        
        
    
        
            
