# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0

    for letter in secret_word:
        if letter in letters_guessed:
            i += 1
            if i == len(secret_word):
                return True
            
    return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lista = []

    for letter in secret_word:
        if letter not in letters_guessed:
            lista.append("_ ")
        else:
            lista.append(letter)
    
    return ''.join(lista)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lista = []

    for letter in string.ascii_lowercase:
        if letter in letters_guessed:
            continue
        lista.append(letter)

    return ''.join(lista)
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guesses = 6
    warnings = 3
    user_guess = ''
    letters = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} long.")
    print(f"You have {warnings} warnings left.")

    while True:
        print(10 * "-")

        if guesses == 0 :
            print(f"You lost! The secret word is: {secret_word}")
            break 
        
        if is_word_guessed(secret_word, letters):
            l_set = set() # letters set
            for l in secret_word:
                l_set.add(l)
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {guesses * len(l_set)}")
            break

        print(f"You have {guesses} guesses left.")
        
        if user_guess:
           print(f"Available letters: {get_available_letters(letters)}")
        else:
           print(f"Available letters: {get_available_letters(list(''))}")

        user_guess = input("Please guess a letter: ")

        if not user_guess.isalpha():
            if warnings >= 0:
               warnings -= 1
            if warnings < 0:
                guesses -= 1
            
            if warnings >= 0:
                print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters)}")
            else:
                print(f"Oops! That is not a valid letter. You have no warnings left so you loose one guess: {get_guessed_word(secret_word, letters)}")

            continue
        
        if user_guess in letters:
            if warnings >= 0:
               warnings -= 1
            if warnings < 0:
                guesses -= 1
            
            if warnings >= 0:
                print(f"Oops! You've already guessed that letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters)}")
            else:
                print(f"Oops! You've already guessed that letter. You have no warnings left so you loose one guess: {get_guessed_word(secret_word, letters)}")

            continue
        
        letters.append(user_guess.lower())
        
        if user_guess.lower() in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters)}")
        else:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters)}")
            if user_guess.lower() in "aeiou":
                guesses -= 2
            else: 
                guesses -= 1


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.split()
    my_word = ''.join(my_word)

    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(my_word)):
        if not my_word[i].isalpha():
            continue
        if my_word[i] == other_word[i]:
            continue
        return False
    
     # quarto caso de uso
    for letter in my_word:
        if not letter.isalpha():
            continue
        if my_word.count(letter) != other_word.count(letter):
            return False
        
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.split()
    my_word = ''.join(my_word)

    list_words = []

    for word in wordlist:
        if len(my_word) == len(word):
            letter_count = 0
            for i in range(len(my_word)):
                if not my_word[i].isalpha():
                    letter_count += 1
                    continue
                if my_word[i] == word[i]:
                    letter_count += 1
            if letter_count == len(word):
                list_words.append(word)
    
    if list_words:
        print(" ".join(list_words))
    else:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    user_guess = ''
    letters = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")

    while True:
        print(10 * "-")

        if guesses == 0 :
            print(f"You lost! The secret word is: {secret_word}")
            break 
        
        if is_word_guessed(secret_word, letters):
            l_set = set() # letters set
            for l in secret_word:
                l_set.add(l)
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {guesses * len(l_set)}")
            break

        print(f"You have {guesses} guesses left.")
        
        if user_guess:
           print(f"Available letters: {get_available_letters(letters)}")
        else:
           print(f"Available letters: {get_available_letters(list(''))}")

        user_guess = input("Please guess a letter: ")

        # adição para 'hangman with hints'
        if user_guess == '*' and match_with_gaps(get_guessed_word(secret_word, letters), secret_word): 
            show_possible_matches(get_guessed_word(secret_word, letters))
            continue

        if not user_guess.isalpha():
            if warnings >= 0:
               warnings -= 1
            if warnings < 0:
                guesses -= 1
            
            if warnings >= 0:
                print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters)}")
            else:
                print(f"Oops! That is not a valid letter. You have no warnings left so you loose one guess: {get_guessed_word(secret_word, letters)}")

            continue
        
        if user_guess in letters:
            if warnings >= 0:
               warnings -= 1
            if warnings < 0:
                guesses -= 1
            
            if warnings >= 0:
                print(f"Oops! You've already guessed that letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters)}")
            else:
                print(f"Oops! You've already guessed that letter. You have no warnings left so you loose one guess: {get_guessed_word(secret_word, letters)}")

            continue
        
        letters.append(user_guess.lower())
        
        if user_guess.lower() in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters)}")
        else:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters)}")
            if user_guess.lower() in "aeiou":
                guesses -= 2
            else: 
                guesses -= 1

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)


    #EU show_possible_matches("a_ pl_ ")
    #EU print(match_with_gaps('a_ ple', 'apple'))

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
