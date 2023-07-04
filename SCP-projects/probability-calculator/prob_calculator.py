import copy
import random

class Hat:
  def __init__(self, **args): # **args é um dicionário que recebe quantidade variável de parâmetros nomeados
          self.contents = []
          
          pares = args.items() # retorna  uma lista de tuplas com os pares chave - valor
    
          # adicionando uma bola para cada quantidade, cada uma como uma string
          for ball, num in pares:
            for _ in range(num):
              self.contents.append(ball)
    
  def draw(self, n):
          if n > len(self.contents):
            return self.contents
               
          balls_out = []
    
          # a cada iteração cria-se um novo índice aleatório e, em seguida, um elemento é removido e adicionado à lista 'balls_out'
          for _ in range(n):
              index_ball = random.randint(0, len(self.contents) - 1)
              balls_out.append(self.contents.pop(index_ball)) # pop retira da lista e retorna o elemento retirado
         
          return balls_out

'''
Objetos compostos são objetos que contém outros objetos em seu interior (listas e instâncias de classe, por exemplo).

- Uma cópia simples('shallow copy' ou cópia rasa), faz uma cópia do objeto composto e insere nesta cópia refências para os objetos contidos no objeto composto de origem.

- Uma cópia profunda('deep copy') copia, recursivamente, tanto os objetos contidos no objeto original como o objeto composto em si.
'''
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  m = 0
  
  # notar que a cada experimento uma cópia profunda do objeto original é criada, fazendo com que os atributos originais ('self.counts', por exemplo) voltem aos valores de início
  # "The balls should not go back into the hat during the draw, similar to an urn experiment without replacement." Significa que não preciso manter o atributo self.contents do jeito que era, posso remover os elementos com 'pop' e deixar como está (vai voltar ao que era de qualquer forma)
  for _ in range(num_experiments):
                
        # cópia do objeto como um todo, incluindo os objetos contidos nele (métodos, atributos ...)
        # a cada iteração cria - se uma nova cópia do objeto original, ou seja, antes do método draw() ser chamado, eu crio uma cópia do objeto original
        hat_copy = copy.deepcopy(hat)
    
        balls_out = hat_copy.draw(num_balls_drawn)

        color_count = 0
    
        for color in expected_balls.keys(): # iterando segundo o número de chaves do dicionário
          if balls_out.count(color) >= expected_balls[color]: # se o número de ocorrências de uma cor na lista for igual ao valor da chave
              color_count += 1

        # se a contagem das cores corresponder à todas as chaves (lembrando que 'color_count' só recebe + 1 se a quantidade exata bater)
        if color_count == len(expected_balls):
              m += 1
          
  # total de ocorrências pelo total de experimentos      
  return m / num_experiments