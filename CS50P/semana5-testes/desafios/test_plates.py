from plates import is_valid

def test_start_with_2_letters():
    assert is_valid("CS") == True
    assert is_valid("5S") == False
    assert is_valid("C5") == False

def test_empty_str():
    assert is_valid("") == False

def test_use_of_numbers():
    assert is_valid("ASD454") == True
    assert is_valid("AS7454") == True
    assert is_valid("AS745D") == False
    assert is_valid("ASD054") == False
    assert is_valid("ASDFG0") == False

def test_size():
    assert is_valid("ASD454") == True
    assert is_valid("AS745") == True
    assert is_valid("AS7") == True
    assert is_valid("AS74566") == False

def test_punctuation_space_etc():
    assert is_valid("AD.444") == False
    assert is_valid("AD,444") == False
    assert is_valid("AD 444") == False
