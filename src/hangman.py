import sys
import random
import globals

# Reads words from the 'words.txt' file and filters them then returns them as a list
def getWords(difficulty):
    
    # Initializing a list to store words obtained from the words.txt file
    rawWords = []

    # Initializing a list to store the filtered words based on the difficulty level
    filteredWords = []

    # Opens the words.txt file in read mode
    with open('../words.txt', 'r') as wfile:
    
        # Iterates through each line and stores each word in the rawWords list
        for line in wfile:
            rawWords = line.lower().split(', ')

    # Iterates through each word in the rawWords list and checks if the word falls in the easy or hard word category
    for word in rawWords:
        if (difficulty.lower() == 'easy' and len(word) <= globals.EASY_WORD_MAXLENGTH) or (difficulty.lower() == 'hard' and len(word) <= globals.HARD_WORD_MAXLENGTH and len(word) > globals.EASY_WORD_MAXLENGTH):
            
            # Stores the filtered word in the filteredWords list  
            filteredWords.append(word)
    
    return filteredWords

# Generates a random word from the filteredWords list
def getRandomWord(difficulty):
    return getWords(difficulty)[random.randint(0, len(getWords(difficulty)) - 1)]

# Replaces each '_' in blanks with the guessed letter
def fillBlanks(letter, word, blanks):
    iterable = 0

    # Loops through each letter of the word 
    while iterable < len(word):

        # Checks if the letter is equal to its consequent letter in the word
        if word[iterable] == letter:

            # Replaces the '_' in the blanks list with that letter
            blanks[iterable] = letter

        # Increments the index iterable
        iterable += 1

    # Prints each element of the blanks list separated by a single whitespace for better visualization
    print('\n' + ' '.join(blanks))

# Displays the starting menu 
def displayMenu():

    print('WELCOME TO HANGMAN IN PYTHON!\n')
    print("Type 'play' to start")
    print("Type 'quit' to exit\n")

# Call this in main.py to play the game
def play(difficulty):

    # This loop stops executing if the user does not wish to play anymore
    while True:

        # Starts the game by displaying the menu on the console
        displayMenu()

        # Taking user input
        choice = input('Enter your choice: ')

        # Dealing with corner cases
        while choice.lower() != 'play' and choice.lower() != 'quit':
            choice = input('Please enter a valid input: ')

        # If the user enters 'play' then we enter the logic of the game
        if choice.lower() == 'play':

            # Checks if user has entered the difficulty level as a command-line argument
            if len(sys.argv) < 2:

                # Prompting the user to enter the difficulty level
                difficulty = input('Please choose the difficulty level (easy/hard): ')
            
            else:
                # Initializing difficulty level as the second command-line argument
                difficulty = sys.argv[1]

            # Dealing with corner cases
            while difficulty.isalpha() == False or difficulty.lower() != 'easy' and difficulty.lower() != 'hard':
                difficulty = input('Please enter a valid difficulty level: ')

            # Generating the word
            word = getRandomWord(difficulty)

            # Storing word length
            word_length = len(word)

            # Initializing a character data type that stores the guessed letter
            letter = ''

            # Initializing the blanks list with the same number of '_' characters as the length of the word
            blanks = ['_']*word_length

            # Initializing misses counter
            misses = 0

            # Initializing guesses counter
            guesses = 0
            
            # This list stores each character that the user guesses correctly
            guessed_letters = []

            # This iterable is used as an index tracker for the guessed_letters list
            iterable = 0

            # For testing purposes
            # Remove the comment below to see the word before guessing
            print('\nThe word is:', word)

            # The loop stops if misses exceed the maximum allowed count or if the user guesses all the letters correctly
            while misses < globals.ALLOWED_MISS_COUNT and guesses != word_length:

                # Taking input from the user
                letter = input('\nPlease enter your guess: ')

                # Dealing with corner cases
                while letter.isalpha() == False or letter == '' or len(letter) > 1:
                    letter = input('Please enter a valid value: ')

                # Printing '_' for each non-guessed letter and replacing each '_' with the right letter after each guess
                fillBlanks(letter=letter, word=word, blanks=blanks)

                # Checks if the letter is present in the word
                if letter not in word:
                    misses += 1
                    print(f'\nYour guess is wrong!\nGuesses = {guesses}\nMisses = {misses}') 
                    
                    # Prints Hangman art
                    print(globals.HANGMANPICS[iterable])
                    iterable += 1

                # Checks if the letter has already been guessed before
                elif letter in word and letter in guessed_letters:
                    print(f'\nYou have already guessed this letter!\nGuesses = {guesses}\nMisses = {misses}')
                
                else:
                    # This loop checks to see if multiple letters inside the word match our guessed letter and increments the number of guesses accordingly
                    for i in word:
                        if letter == i:
                            guesses += 1
                            
                    # Adds the guessed letter to our guessed_letters array         
                    guessed_letters.append(letter) 
                    
                    print(f'\nYour guess is right!\nGuesses = {guesses}\nMisses = {misses}')                    

            # Win/Lose prompts
            if misses == globals.ALLOWED_MISS_COUNT:
                print('\nYou have lost the game :(. Better luck next time!')
            else:
                print('\nYou have won the game :). Good Work!')

            # Asks the user if they wish to play again
            choice = input('\nDo you want to play again? (Y/n) ')
            if choice.lower() == 'y':
                print()
                pass
            else:
                break

        # If the user enters 'quit' the above loop is skipped
        if choice == 'quit':
            break