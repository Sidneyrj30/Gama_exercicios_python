'''Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.'''

numero = input("Digite um número: ")

def count_num(numero):
    if numero.isdigit():
        sum = 0
        for i in numero:
            sum += 1
        return f"A quantidade de digitos é: {sum}"
    else:
        return 'Valor errado'

sum = count_num(numero)

print(sum)