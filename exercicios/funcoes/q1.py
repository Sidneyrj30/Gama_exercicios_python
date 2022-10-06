import os

# def print_number(numero):
#     valor = 1
#     while valor <= numero:
#         for item in range(valor):
#             print(valor, end=' ')
#         print("")
#         valor += 1

def print_numero(valor):
    for item in range(1, valor + 1):
        print(f"{(str(item)+' ') * item}")


os.system('cls')

numero = int(input("Digite um numero: "))

print_numero(numero)


