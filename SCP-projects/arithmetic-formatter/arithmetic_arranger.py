import re

# todo parâmetro nomeado é opcional
def arithmetic_arranger(problems, result = False):
    n1 = []
    n2 = []
    sinais = []
    espaco = '    '
    arranged_problems = []
    results = []
    
    if len(problems) > 5:
      return 'Error: Too many problems.'

    # criando as listas que serão unidas e convertidas em strings
    for problem in problems:
      
      # validando as entradas
      p = re.search(r'^(.+) (.{1}) (.+)$', problem)

      if p.group(2) not in '+-':
        return "Error: Operator must be '+' or '-'."
      try:
        num1 = int(p.group(1))
        num2 = int(p.group(3))
        if len(p.group(1)) > 4 or len(p.group(3)) > 4:
          return 'Error: Numbers cannot be more than four digits.'
      except ValueError:
        return 'Error: Numbers must only contain digits.'

      # lista de resultados para caso o segundo argumento seja True
      if p.group(2) == '+':
        results.append(str(num1 + num2))
      else:
        results.append(str(num1 - num2))

      # criando as listas que sempre constarão no resultado
      n1.append(str(num1))
      n2.append(str(num2))
      sinais.append(p.group(2))

    # formatando os operandos e os sinais e atualizando as listas 
    for i in range(len(n1)):
       new_n1, new_n2 = add_spaces_to_the_minor(n1[i], n2[i])
       n1[i] = new_n1
       n2[i] = new_n2
       
       new_n2 = add_sinal_to_n2(n2[i], sinais[i])
       n2[i] = new_n2
  
       new_n1 = compensate_n1(n1[i], n2[i])
       n1[i] = new_n1

    # criando a lista com as barras após as expressões
    dashes = []
    for i in range(len(n1)):
      if len(n1[i]) >= len(n2[i]):
        dashes.append(len(n1[i]) * '-')
      elif len(n2[i]) > len(n1[i]):
        dashes.append(len(n2[i]) * '-')

    # atualizando a lista com todos os caracteres em ordem para transformar tudo em string
    for x in n1:
      arranged_problems.append(x)
      if n1.index(x) != len(n1) - 1:
         arranged_problems.append(espaco)
    arranged_problems.append('\n')
    for y in n2:
      arranged_problems.append(y)
      if n2.index(y) != len(n2) - 1:
         arranged_problems.append(espaco)
    arranged_problems.append('\n')
    for z in dashes:
      arranged_problems.append(z)
      if dashes.index(z) != len(dashes) - 1:
        arranged_problems.append(espaco)

    
    # [GAMBIARRA] para o problema com as barrinhas '-'
    if len(problems) != 2 or len(problems) == 2 and result:
        arranged_problems.pop()
    
    # atualizando a lista também com os resultados, caso necessário exibí-los
    if result:
       arranged_problems.append('\n')
       for i in range(len(dashes)):
         dif = len(dashes[i]) - len(results[i])
         results[i] = dif * ' ' + results[i]
       for v in results:
         arranged_problems.append(v)
         if results.index(v) != len(results) - 1:
             arranged_problems.append(espaco)
           
    arranged_problems = ''.join(arranged_problems)

    return arranged_problems

def add_spaces_to_the_minor(n1, n2):
    dif = ''
  
    if len(n1) > len(n2):
        dif = (len(n1) - len(n2)) * ' ' + 2 * ' '
        n2 = dif + n2
    elif len(n2) > len(n1):
        dif = (len(n2) - len(n1)) * ' ' + 2 * ' '
        n1 = dif + n1

    return (n1, n2)

def add_sinal_to_n2(n2, sinal):
    npoints = 0
  
    for char in n2:
      if char == ' ':
          npoints += 1

    if npoints == 0:
      n2 = sinal + ' ' + n2
    elif npoints == 1:
      n2 = sinal + n2
    else:
      n2 = list(n2)
      n2[0] = sinal
      n2 = ''.join(n2)
      
    return n2

def compensate_n1(n1, n2):
    dif = ''
  
    if len(n1) > len(n2):
        dif = (len(n1) - len(n2)) * ' '
        n2 = dif + n2
    elif len(n2) > len(n1):
        dif = (len(n2) - len(n1)) * ' '
        n1 = dif + n1

    return n1