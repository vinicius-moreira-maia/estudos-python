s = input("Greeting: ").lower().strip()

if "hello" in s:
    print("$0")
elif s.startswith("h") and "hello" not in s:
    print("$20")
else:
    print("$100")