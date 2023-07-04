import copy

# em Python, o operador de atribuição não cria uma cópia entre dois objetos, cria um vínculo entre eles.
# Muitas vezes, em coleções mutáveis, cópias de verdade precisam ser criadas para que a modificação de um objeto não
# modifique também o outro.


# em tipos que não são coleções mutáveis isso aparentemente não importa tanto

a = 8
b = a

print(a is b) # -> True

a = 2 # a e b deixam, agora, de ser os mesmos objetos

print(a is b) # -> False

print('-------------------------')

x = [2, 3, 7]
y = x

print(x is y) # -> True

x[0] = 0 # modifica também em y, por ser o mesmo objeto

print(x is y) # -> True

y[0] = 21 # modifica também em x, por ser o mesmo objeto

print(x is y) # -> True

# SOLUÇÃO
print('-------------------------')

y = copy.deepcopy(x) # -> copia o objeto que contém e os objetos que fazem parte
print(x is y) # -> False !! Agora são objetos completamente distintos