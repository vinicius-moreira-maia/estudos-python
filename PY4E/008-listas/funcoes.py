# instanciando um objeto da classe 'list'
nums = list() # ou nums = []

while True:
    try:
       n = input('Número: ')
       if n == "ok":
           break
       else:
          n = float(n)
          nums.append(n)
    except ValueError:
       print('digite um número!')
       continue 

print(f"Números: {nums}")
print(f"Média: {sum(nums) / len(nums)}")