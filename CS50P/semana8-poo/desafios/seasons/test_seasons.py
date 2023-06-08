from seasons import minutos_extenso
from datetime import date

def test_output():
    assert minutos_extenso(date(1993, 10, 27)) == "Fifteen million, three hundred eighty-two thousand eighty minutes"
