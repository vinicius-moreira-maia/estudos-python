conta = {'Zé' : 456, 'Zézé' : 111, 'Zézim' : 4678}

# o método get() retorna o valor da chave passada como parâmetro, o segundo parâmetro é o retorno caso a chave não esteja no dicionário
print(conta.get('Zé', 'não consumiu'))
print(conta.get('Jubão', 'não consumiu'))