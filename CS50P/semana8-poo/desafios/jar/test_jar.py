# testar métodos não é tão simples quanto testar funções! -> 'mock' (não sei o que é mock, mas foi mencionado)

from jar import Jar # importando a classe
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10

def test_str():
    jar = Jar(10)
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(7)
    assert jar.size == 7 # método getter

def test_deposit_value_error():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4

def test_withdraw_value_error():
    jar = Jar(10)
    jar.deposit(7)
    with pytest.raises(ValueError):
        jar.withdraw(8)
