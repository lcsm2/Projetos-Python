#PROJETO PEDRA PAPEL E TESOURA
import random
print("Seja bem-vindo ao peojeto pedra papel e tesoura.")

user_point = 0
pc_points = 0
choice = ["a", "b", "c"]
while True:
    user_choice = input("Escolha (A)Pedra, (B)Papel e (C)Tesoura, ou (D)Sair do jogo: ").lower()
    
    if user_choice == "d":
        break

    if user_choice not in choice:
        continue
    
    pc = random.randint(0,2)
    pc_choice = choice[pc]

    print("O computador escolheu " + pc_choice)

    if user_choice == pc_choice:
        print("Empate!")
    elif user_choice == "a" and pc_choice == "c":
        print("Você Ganhou!")
        user_point = user_point + 1
    elif user_choice == "b" and pc_choice == "a":
        print("Você Ganhou!")
        user_point = user_point + 1
    elif user_choice == "c" and pc_choice == "b":
        print("Você Ganhou!")
        user_point = user_point + 1
    else:
        print("Você perdeu!")
        pc_points = pc_points + 1

print("Sua pontuação: " + str(user_point))
print("A pontuação do pc é : " + str(pc_points))

if user_point == pc_points:
    print(f"Jogo acabou empatado, Usuário {user_point} pontos, Máquina {pc_points} pontos.")
elif user_point > pc_points:
    print(f"Você ganhou o jogo, Usuário {user_point} pontos, Máquina {pc_points} pontos.")
else:
    print(f"Você perdeu o jogo, Usuário {user_point} pontos, Máquina {pc_points} pontos.")