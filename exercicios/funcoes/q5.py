'''Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, 
que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
 A função “altera” o valor de custo para incluir o imposto sobre vendas.'''

print("IMPOSTO")

taxa = int(input("Qual taxa do imposto em porcentagem: "))
custo = int(input("Qual o custo: "))

def somaImposto(taxa, custo):
    taxa_convertida = taxa / 100 + 1
    preco_com_imposto = custo * taxa_convertida

    print(f"A soma do custo com o imposto é: {preco_com_imposto:.2f}")

somaImposto(taxa, custo)