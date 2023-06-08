# runtime errors - erros em tempo de execução

try:
  # sempre deixar o mínimo possível de linhas no try
  x = int(input("X: "))
  # print(f"X: {x}")
except ValueError:
  print("x não é um inteiro")
else: # o else serve como uma cláusula para caso não ocorra erros
  print(f"X: {x}")