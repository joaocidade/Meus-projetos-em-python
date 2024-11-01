import random
def jogar():
    escolha_maquina()
    desafios_lista()
    print('Bem vindo ao ASND')
    print('vamos começar')
    print('digite 1 para começar')
    print('digite 2 para sair')
    inicio = int(input(''))

    if(inicio == 1):
        print('iniciando o jogo')
    else:
        print('voce nao tem essa opção')
        return inicio
def escolha_maquina():
    return random.randint(1,3)

def desafios_lista():
    desafios = [1,2,3]
def perguntas_lista():
    perguntas_could = ['I ____ speak English','I ____ run very fast.','You ____ work 7 days per week.','You ____ play the piano.','He ____ understand English. ''It ___ happen with you too. ','My sister ___ sing. ','We ___ see very well at night. ','Anyone ___ make this wrong.   ','My sister ___ dance with you. ''He may not ___ come next week. ','I haven’t ____ sleep well recently.   ','Are you going ____ to sell this old car? ','You should ____ do that in less than an hour. ','They have ____ come here every day. ']
    lista_enumerada = enumerate(perguntas_could)
    print(lista_enumerada)
perguntas_lista()
jogar()