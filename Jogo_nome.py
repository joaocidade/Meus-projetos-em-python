import random

escolha_maquina = random.randint(0,10)
print('Bem vindo ao meu jogo')
print('por favor eslha uma opção e tente adivinhar o nome do jogador: ')
lista_nomes = ['0 = joao','1 = pedro','2 = maria','3 = felipe','4 = ana','5 = francisco','6 = matheus','7 = guilerme','8 = nicolas','9 = prupru', '10 = vitor']

for indice, nome in enumerate(lista_nomes):
    
    print(f'{nome} escolheu {escolha_maquina}')
    
escolha_player = str(input('digite um nome: '))

if  escolha_player == escolha_maquina:
    print('vitoria!')
else:
        print('derrota!')
