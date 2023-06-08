import validators

def main():
    r = validators.email(input("What's your email address? "))

    if r:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()