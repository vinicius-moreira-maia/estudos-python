def main():
    print(value(input("Greeting: ")))

def value(greeting):
    greeting = greeting.lower() # .lower() causaria erro de asserção caso estivesse em main(), já que o método estaria sendo usado fora da função que está sendo testada -> um exemplo de como a modularização é importante
    if greeting.startswith("hello"):
        return 0
    elif "hello" not in greeting and greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()