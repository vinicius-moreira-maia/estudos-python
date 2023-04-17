# arquivo sem os comentários

import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline() # readline() retorna uma linha do arquivo (que aparentemente tem só uma linha)
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    i = 0

    for letter in secret_word:
        if letter in letters_guessed:
            i += 1
            if i == len(secret_word):
                return True
            
    return False



def get_guessed_word(secret_word, letters_guessed):
    lista = []

    for letter in secret_word:
        if letter not in letters_guessed:
            lista.append("_ ")
        else:
            lista.append(letter)
    
    return ''.join(lista)



def get_available_letters(letters_guessed):
    lista = []

    for letter in string.ascii_lowercase:
        if letter in letters_guessed:
            continue
        lista.append(letter)

    return ''.join(lista)
    
    

def hangman(secret_word):
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


def match_with_gaps(my_word, other_word):
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

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
