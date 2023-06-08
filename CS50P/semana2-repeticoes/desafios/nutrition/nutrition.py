frutas = {'apple':130,
          'avocado':50,
          'banana':110,
          'cantaloupe':50,
          'grapefruit':60,
          'grapes':90,
          'honeydew melon':50,
          'kiwifruit':90,
          'lemon':15,
          'lime':20,
          'nectarine':60,
          'orange':80,
          'pach':60,
          'pear':100,
          'pineapple':50,
          'plums':70,
          'strawberries':50,
          'sweet cherries':100,
          'tangerine':50,
          'watermelon':80
}

def main():
    while True:
        f = input('Item: ').lower().strip()
        if f in frutas: # 'in' aqui é uma hash function! O(1) -> dicionário é uma hash table
            print(f'Calories: {frutas[f]}')
            return 0
        else:
            return 1

main()