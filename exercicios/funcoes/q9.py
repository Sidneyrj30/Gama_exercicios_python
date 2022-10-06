"Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721."

def inverter(txt):
  return txt[::-1]

texto = input("Digite algo: ")
texto_invertido = inverter(texto)

print(f"O número invertido é: {texto_invertido}")


