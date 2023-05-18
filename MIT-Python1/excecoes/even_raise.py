def findAnEven(L):

    # levanta exceção AssertionError caso o teste lógico falhe (encerra a função)
    assert len(L) < 5, 'to many values on list'

    for n in L:
        if n % 2 == 0:
            return n
        else:
            raise ValueError("integer not found") # encerra a função

try:
    print(findAnEven([3, 5, 7, 11, 0, -1])) 
except (ValueError, AssertionError) as msg:
    print(msg)