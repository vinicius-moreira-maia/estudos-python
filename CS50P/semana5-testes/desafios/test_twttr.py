from twttr import shorten

def test_upper():
    assert shorten("ARARAQUARA") == "RRQR"

def test_lower():
    assert shorten("araraquara") == "rrqr"

def test_with_other_chars():
    assert shorten("Guarda-Chuva") == "Grd-Chv"

def test_empty_str():
    assert shorten("") == ""

def test_no_letters():
    assert shorten("1243--") == "1243--"

def test_with_punctuation():
    assert shorten("oirr, camarada!") == "rr, cmrd!"
