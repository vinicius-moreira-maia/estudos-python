from oi import oi

def test_default():
    assert oi() == "oi, mundo"

def test_argument():
    assert oi("Vini") == "oi, Vini"

