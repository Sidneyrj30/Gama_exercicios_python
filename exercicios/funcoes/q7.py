'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

import os

os.system('cls')

def valorPagamento(prestacao, dias_atraso=0):
    if dias_atraso == 0:
        print(f'O valor da prestação é: R${prestacao}')
        
    elif dias_atraso > 0:
        prestacao = prestacao * 1.03 + (0.001 * dias_atraso)
        print(f'O valor da prestação é: R${prestacao:.2f}')
    return prestacao

prestacao = 1
relatorio = []

while prestacao != 0:
    if prestacao > 0:
        prestacao = float(input("Qual o valor da prestação: "))
        dias_atraso = int(input("Qual o número de dias em atraso: "))

        valor = valorPagamento(prestacao, dias_atraso)

        relatorio.append(valor)
i = 0
total = 0
for item in relatorio:
    i += 1
    total += item

print(f"Relatório final: {i} prestações pelo total de R${total}")

