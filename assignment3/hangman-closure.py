# Task 4:

def make_hangman(secret_word):
    
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter)
        
        display_word = ""
        
        for char in secret_word:
            if char in guesses:
                display_word += char
            else:
                display_word += "_"
        
        print(display_word)
        
        return "_" not in display_word
        
        
        
    return hangman_closure


# user input
secret = input("Enter secret word: ")

# Game Logic
game = make_hangman(secret)

while True:
    guess = input("Enter a letter: ")
    done = game(guess)

    if done:
        print("You guessed the word!")
        break
