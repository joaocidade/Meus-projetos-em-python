import random

def escolha_maquina():
    return random.randint(1, 3)

def desafios_lista(escolha):
    desafios = [1, 2, 3]
    if escolha in desafios:
        print('Vitória!')
    else:
        print('Desafio não encontrado.')

def jogar():
    print('Bem-vindo ao ASND!')
    print('Vamos começar...')
    print('Digite 1 para começar')
    print('Digite 2 para sair')
    
    inicio = int(input(''))
    
    if inicio == 1:
        print('Iniciando o jogo...')
        escolha = escolha_maquina()
        print(f'A máquina escolheu: {escolha}')
        desafios_lista(escolha)
    else:
        print('Você não tem essa opção.')

jogar()