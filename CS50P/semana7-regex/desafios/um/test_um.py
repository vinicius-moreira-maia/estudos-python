from um import count

def test_just_um():
    assert count("um") == 1

def test_begin_and_end_phrase():
    assert count("Um cara matou um.") == 2

def test_begin_and_end_and_middle_phrase():
    assert count("Um cara, um, matou um.") == 3

def test_um_in_a_word():
    assert count("Umbabarauma, homem gol!") == 0