import random

def escolha_maquina():
    return random.randint(1, 5)

def escolha_player():
    while True:
        try:
            escolha2 = int(input('Escolha uma opção (1 = pedra, 2 = tesoura, 3 = papel, 4 = lagarto, 5 = Spock): '))
            if escolha2 in [1, 2, 3, 4, 5]:
                return escolha2
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def verificar_resultado(escolha1, escolha2):
    if escolha1 == 1 and (escolha2 == 3 or escolha2 == 5):
        return True
    if escolha1 == 2 and (escolha2 == 1 or escolha2 == 5):
        return True
    if escolha1 == 3 and (escolha2 == 2 or escolha2 == 4):
        return True
    if escolha1 == 4 and (escolha2 == 1 or escolha2 == 2):
        return True
    if escolha1 == 5 and (escolha2 == 4 or escolha2 == 3):
        return True
    return False

def jogar():
    while True:
        escolha1 = escolha_maquina()
        escolha2 = escolha_player()
        print("A escolha da máquina foi: {}".format(escolha1))

        if verificar_resultado(escolha1, escolha2):
            print('Você acertou, parabéns!')
            break
        else:
            print('Você errou, tente novamente.')
            print('A escolha certa era', escolha1)

jogar()
