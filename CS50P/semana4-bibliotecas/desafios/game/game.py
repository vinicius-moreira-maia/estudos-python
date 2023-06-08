import random

def main():
    n = get_num()

    while True:
        guess = get_guess()
        if guess > n:
            print("Too large!")
        elif guess < n:
            print("Too small!")
        else:
            print("Just right!")
            return 0

def get_num():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            else:
                return random.randint(1, level)
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                raise ValueError
            else:
                return guess
        except ValueError:
            pass

if __name__ == "__main__":
    main()