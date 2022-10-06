import os

# def print_numero(valor):
#     numero = 1
#     while numero <= valor:
#         for i in range(1,numero + 1):
#             print(i, end=' ')
#         print(' ')
#         numero += 1


def print_numero_texto(valor):
    numero = 1
    texto = str(numero)
    print(texto)
    while numero < valor:   
        texto = texto + ' ' + str(numero + 1)
        print(texto)
        numero += 1

os.system('cls')

numero = int(input("Digite um numero: "))

print_numero_texto(numero)


