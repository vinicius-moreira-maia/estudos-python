largest = None
smallest = None

while True:
    try:
      num = input("Enter a number: ")
      if not num.isdigit():
        raise ValueError
      else:
        smallest = int()
      if num == "done":
        break
    except ValueError:
        print("Invalid input")
        pass
    if num == "done":
        break

    if largest is None or largest < int(num):
        largest = num
    if smallest is None or smallest > int(num):
        smallest = num

print("Maximum is", largest)
print("Minimun is", smallest)