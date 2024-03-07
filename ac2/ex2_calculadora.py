"""
Exercício 2: salário
Desenvolva uma função em Python cujo nome é calcula_salario. 
Essa função recebe dois parâmetros posicionais reais, valor_hora e num_horas, 
que correspondem ao valor do salário por hora e o número de horas trabalhadas no mês, 
respectivamente. Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, 
cujo valor padrão é 0.275. A função retorna o salário líquido de um funcionário, 
calculado como o produto do valor por hora pelo número de horas, reduzido o percentual do imposto de renda dado.
"""

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    
    salario_liquido = (valor_hora * num_horas) * irpf

    return salario_liquido

def main():
    print(calcula_salario(2, 10))

main()