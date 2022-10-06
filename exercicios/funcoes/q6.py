'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, 
o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, 
a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.'''

import os

def converter_hora():
    horaint = int(hora)
    if horaint > 12:
        horario = str(horaint - 12) + ':'+ minuto +' P.M'
    elif horaint == 12:
        horario = str(horaint) + ':'+ minuto +' P.M'
    elif horaint < 12:
        horario = str(hora)+':'+str(minuto)+' A.M'
    return horario

os.system('cls')

# horario = input("Digite o horário nesse formato [hh:mm]: ")
# horario = horario.split(':')

# hora = horario[0]
# minuto = horario[1]

hora = input("Digie a hora: ")
minuto = input("Digie o minuto: ")

if hora.isdigit() and minuto.isdigit():
    print(converter_hora())
else:
    print("Digitou errado")



