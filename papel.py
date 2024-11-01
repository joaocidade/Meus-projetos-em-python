import random

def escolha_maquina():
    escolha1 = random.randint(1,3)
    print(escolha1)

def escolha_player():
    escolha_maquina()
    escolha2 = int(input('escolha uma opção: '))
    
    if escolha1 == escolha2:
        print('voce acertou, parabens')
    else:
        print('voce errou, tente novamente')

        
print('bem vindo ao jogo do pedra, papel e tesoura')
print('escolha uma opção')
print('1 = pedra')
print('2 = tesoura')
print('3 = papel')

escolha_maquina()
escolha_player()