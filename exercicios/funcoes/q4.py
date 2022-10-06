'''Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere P, se seu argumento for positivo, e N, 
se seu argumento for zero ou negativo.'''


def positivo_negativo(valor):
    if valor > 0:
        print("P")
    else:
        print("N")


valor = int(input("Digite um número: "))

positivo_negativo(valor)
