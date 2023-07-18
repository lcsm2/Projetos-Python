import random
print("Seja bem-vindo ao projeto de Adivinhação de números!")

numero = input("Digite o número máximo do desafio: ")

if numero.isdigit():     #Aqui verificamos se o número é realmente um número e transformamos ele em inteiro(int),
    numero = int(numero) #pois quando ele é escrito no input ele está como string!
else:
    print("Erro. O valor anterior informado não é um número, \
    por favor coloque um valor correto.")
    quit()

numero_aleatorio = random.randint(0, numero)

tentativas = 1

while True:
    pergunta = input("Advinhe o número: ")
    if pergunta.isdigit():
        pergunta = int(pergunta)
    else:
        print("Por favor coloque um valor numérico.")
        continue

    if  pergunta == numero_aleatorio:
        print(f"Você acertou o número com um total de {tentativas}")   
        break
    elif pergunta > numero_aleatorio:
        print("O número randômico é menor que isso...")
        tentativas = tentativas + 1
    else:
        print("O número randômico é maior que isso...")
        tentativas = tentativas + 1
