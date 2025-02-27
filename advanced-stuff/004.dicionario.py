texto = '''Era uma casa, uma casa bem antiga, uma casa que todos na vila conheciam como a casa assombrada. Dentro da casa, havia um quarto, um quarto escuro, um quarto onde ninguém queria entrar. No meio do quarto, havia uma cadeira, uma cadeira velha, uma cadeira que rangia sempre que o vento passava pela janela, uma janela quebrada, uma janela que deixava a lua iluminar a cadeira, a casa e o quarto.'''

texto_editado = texto.replace(".", "").replace(",", "")

palavra = ""
palavras = {}
for caractere in texto:
    if caractere != " ":
        palavra += caractere
    else:
        palavras[palavra] = palavras.get(palavra, 0) + 1 
        palavra = ""

print(palavras)
        