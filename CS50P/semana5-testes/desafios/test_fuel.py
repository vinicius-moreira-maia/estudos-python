from fuel import gauge, convert
import pytest

# TESTAR FUNÇÕES QUE LEVANTAM EXCEÇÕES DE FORMA NÃO DELIBERADA, OU SEJA, QUANDO EU LIDO COM AS EXCEÇÕES NA PRÓPRIA FUNÇÃO, CAUSA CONFUSÃO NA HORA DE TESTÁ-LAS NO PYTEST, POIS ELE ACUSA QUE A EXCEÇÃO AQUI LEVANTADA GEROU OUTRA EXCEÇÃO NA FUNÇÃO DA UNIDADE QUE ESTÁ SENDO TESTADA
def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

# TESTAR FUNÇÕES QUE LEVANTAM EXCEÇÕES DE FORMA NÃO DELIBERADA, OU SEJA, QUANDO EU LIDO COM AS EXCEÇÕES NA PRÓPRIA FUNÇÃO, CAUSA CONFUSÃO NA HORA DE TESTÁ-LAS NO PYTEST, POIS ELE ACUSA QUE A EXCEÇÃO AQUI LEVANTADA GEROU OUTRA EXCEÇÃO NA FUNÇÃO DA UNIDADE QUE ESTÁ SENDO TESTADA
def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/5")

def test_convert_valid_input():
    assert convert("3/4") == 75
    assert convert("4/4") == 100

def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(75) == "75%"