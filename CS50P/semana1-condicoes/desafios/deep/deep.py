n = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if n in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")