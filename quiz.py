print("Seja bem-vindo ao projeto Quiz!")

pergunta_usuario = input("Podemos começar? (sim/não): ")
if pergunta_usuario != "sim":
    quit()
score = 0

print("Começando...")
print("Qual foi a empresa que desenvolveu o jogo Grand Theft Auto (GTA)? \
\n (A)Rockstar Games \n (B)Mojang \n (C)Microsoft \n (D)Ubisoft \n (E)Xbox \n")
resposta1 = input("Resposta: ")

if resposta1 == "A":
    print("Resposta correta! :)")
    score = score + 1
else:
    print("Você errou a questão! :(")
    score = score -1 

print("Qual foi o ano que Minecraft foi lançado? \
\n (A)2020 \n (B)2015 \n (C)2009 \n (D)2004 \n (E)2010 \n")
resposta2 = input("Resposta: ")

if resposta2 == "C":
    print("Resposta correta! :)")
    score = score + 1
else:
    print("Resposta de Paulo! :(")
    score = score - 1

print(f"O quiz acabou. Sua pontuação total foi de {score}.")