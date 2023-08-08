ing2port = dict()

# senão houver um item de chave 'one' ele é adicionado automaticamente
ing2port['one'] = 'um'


# a ordem dos itens de um dicionário era irrelevante (ERA)
ing2port = {'one' : 'um', 'two' : 'dois', 'three' : 'três', 'four' : 'quatro'}

# retorna o número de pares chave - valor
print(len(ing2port))

# se há ou não a chave 'two' (hash function)
print('two' in ing2port)

