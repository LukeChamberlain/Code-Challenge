import random

print(f"\nWelcome to Hangman!\n")
words =  ["code", "file", "selection", "view", "terminal", "challenge", "chrome", "british", "football", "cougars"]
word_of_choice = random.choice(words)

def word_to_underscores(word_of_choice):
    letters = ""
    letters += " _"*len(word_of_choice)
    return letters

word_selected = word_to_underscores(word_of_choice)

print(word_selected)
print(word_of_choice)
            
