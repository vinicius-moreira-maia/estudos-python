def sumDigits(s):
    total = 0
    for char in s:
        try:
            total += int(char)
        except ValueError:
            pass
    
    return total

print(sumDigits('a2b3c'))