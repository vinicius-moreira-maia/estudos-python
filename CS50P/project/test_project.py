from project import valid_input, get_dimensions, shape_char
from rectangles import Rectangle, Square

def test_valid_dimensions():
    assert valid_input('2 x 2') == True
    assert valid_input('02 x 02') == True
    assert valid_input('10 x 6') == True
    assert valid_input('10 x 10') == True

def test_invalid_dimensions():
    assert valid_input('002 x 2') == False
    assert valid_input('11 x 2') == False
    assert valid_input('1 x 6') == False
    assert valid_input('cat') == False

def test_get_dimensions():
    assert get_dimensions('02 x 10') == (2, 10)
    assert get_dimensions('2 x 10') == (2, 10)
    assert get_dimensions('10 x 10') == (10, 10)
    assert get_dimensions('2 x 2') == (2, 2)

def test_shape_char():
    assert shape_char(Square(3)) == {'Area': 9,'Perimeter': 12, 'Diagonal': 4.24}
    assert shape_char(Rectangle(4, 5)) == {'Area': 20,'Perimeter': 18, 'Diagonal': 6.4}