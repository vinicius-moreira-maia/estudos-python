from bank import value

def test_hello_in_the_beginning():
    assert value("hello, my friend") == 0

# erro no pytest RESOLVIDO
def test_hello_in_the_beginning_upper():
    assert value("HELLO, my friend") == 0

def test_nothing():
    assert value("") == 100

def test_hello_in_the_end():
    assert value("my friend, hello") == 100

# erro no pytest RESOLVIDO
def test_hello_in_the_end_upper():
    assert value("my friend, HELLO") == 100

def test_no_hello_but_h():
    assert value("hi, dude") == 20

# erro no pytest RESOLVIDO
def test_no_hello_but_h_upper():
    assert value("HI, dude") == 20