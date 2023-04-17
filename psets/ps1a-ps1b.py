# A parte C não foi feita (nem será). 

''' calcular quantos meses levarei pra juntar o dinheiro da entrada '''

def main():

    # poupança
    current_savings = 0

    # pegando os inputs
    annual_salary, portion_saved, total_cost = get_inputs()
    
    # entrada
    portion_down_payment = 0.25 * total_cost
    
    # Número aproximado de meses
    m = months(current_savings, annual_salary, portion_saved, portion_down_payment) 

    print(f'Number of months: {m}')

def get_inputs():
    
    annual_salary = float(input("Enter your annual salary: "))

    # porcentagem do salário dedicada à poupança
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

    # valor da casa
    total_cost = float(input("Enter the cost of your dream home: "))

    return (annual_salary, portion_saved, total_cost)

def months(current_savings, annual_salary, portion_saved, portion_down_payment):

    # a poupança rende 4% ao ano
    r = 0.04
    
    # salário mensal a ser depositado
    amt_of_salary_per_month = annual_salary / 12 * portion_saved  

    m = 0

    while current_savings < portion_down_payment:

        # PART B -> calculando com aumento de 3% no salário a cada 6 meses
        if m > 0 and m % 6 == 0:
            amt_of_salary_per_month += amt_of_salary_per_month * 0.05
        
        # adicionando a fração do salário guardada por mês na poupança
        current_savings += amt_of_salary_per_month

        # calculando e somando o rendimento mensal da poupança
        current_savings += current_savings * r / 12
        
        m += 1

    '''
    Acredito que há a diferença de um mês em alguns casos por conta da diferença entre a poupança e o valor da entrada. Talvez não esteja sabendo fazer a aproximação de forma precisa.
    
    '''  

    #print(current_savings - portion_down_payment)
    #print(current_savings)
    #print(portion_down_payment)

    return m

if __name__ == '__main__':
    main()