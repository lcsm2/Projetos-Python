import random
print("Seja bem-vindo ao projeto de Adivinhação de números!")

numero = input("Digite o número máximo do desafio: ")
if numero.isdigit():
    numero = int(numero)
else:
    print("Erro: o valor que foi informado não é numérico. \
 Por favor execute o código novamente e coloque um valor numérico")
quit()

numero_aleatorio = random.randint(0, numero)