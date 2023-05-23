# TESTES AUTOMATIZADOS (testam a lógica)

# TDD (Test Driven Development) é sobre escrever testes antes do código

# o ideal é ter uma bateria de testes que cobre o máximo possível do software (cobrir todas as linhas de código)
# foco nos casos que podem gerar erros (explorar os caminhos do código)
# a ideia é, rotineiramente, executar a bateria de testes (várias vezes ao dia)

# Arcabouço de Testes Automatizados (pytest, no caso)

# pytest + "test_<nome_do_arquivo>"

# digitando só 'pytest' no terminal, ele procura todos os arquivos que começam com "test_" e executa todas as funções que também possuem "test_" no começo

# considera classes do tipo Test*

def func(x):
    return x + 1

# Função de teste ("test_" no início sempre)
def test_func():
    assert func(3) == 4