import random

def jogar(escolha_player, escolha_maquina):
    if escolha_player < escolha_maquina:
        print('o numero é maior que o escolhido: ')
        return False
    elif escolha_player > escolha_maquina:
        print('o numero é menor que o escolhido: ')
        return False
    else:
        print('voce venceu')
        return True

print('escolha um numero de 1 a 10:')
escolha_player = int(input('digite o numero: '))

escolha_maquina = random.randint(1,10)

if escolha_player == escolha_maquina:
    print('vitoria!')
else:
    while not jogar(escolha_player, escolha_maquina):
        print('derrota!')
        escolha_player = int(input('tente novamente: '))
        
    

