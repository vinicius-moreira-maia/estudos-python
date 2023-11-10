'''
Encapsulamento é o "envelope" dos dados, contendo também os métodos que operam nesses dados. Information Hidding é alguma informação interna que não pode ser diretamente acessada, sob o risco de problemas ocorrerem com mudanças indevidas. Ambos os conceitos são independentes, mas quando ambos estão presentes, há Data Abstraction, que é o termo mais amplo.

Data Abstraction = Data Encapsulation + Data Hidding.
'''

# Encapsulamento é conseguido através dos métodos getter e setter.

class Pessoa:
    def __init__(self, nome = ""):
        self.nome = nome
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome

    # Em linhas gerais, __repr__ e __str__ são iguais, a diferença é que o retorno de repr pode ser lido como comandos em Python, enquanto str é só uma string.
    def __repr__(self):
        return f"Pessoa('{self.nome}')"

    def __str__(self):
        return f"Nome da pessoa: {self.nome}"

  
if __name__ == "__main__":
   p = Pessoa("João")
   p_repr = repr(p) # repr procura o __repr__ da classe.
   print(p_repr, type(p_repr))

   # O retorno de __repr__ pode ser lido como código Python, e no caso ele retorna um novo objeto.
   p2 = eval(p_repr) 
   print(p2) # Aqui é o método str que é chamado.
   print(type(p2))

# O Python procura os métodos str ou repr na classe de definição do objeto quando ele é diretamente incluído em uma saída, caso não encontre, uma saída contendo o endereço de memória surgirá.

# repr -> Usado em representações internas, para serem lidas pelo interpretador.
# str -> Usado para mostrar informações aos usuários.