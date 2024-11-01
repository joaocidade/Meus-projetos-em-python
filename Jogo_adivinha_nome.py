import random 
def escolha_palavra():
    palavra = ['python','java','kotlin','javascript']
    return random.choice(palavra).upper()

def jogo():
    palavra = escolha_palavra()
    letras_adivinhadas = []
    tentativas = 6
    
    print('bem vindo ao jogo')
    print('_ '* len(palavra))
    
    while tentativas > 0:
        tentativa = input('digite uma letra ').upper()
        
        if tentativa in letras_adivinhadas:
            print('voce ja tentou esta letra ')
            continue
        
        letras_adivinhadas.append(tentativa)
        
        if tentativa in palavra:
            print('voce acertou uma letra')
        else:
            tentativas -= 1
            print('voce errou, tente novamente, você tem {} tentativas' .format(tentativas))
        
        palavra_oculta = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
        print(' '.join(palavra_oculta))
    
        if '_' not in palavra_oculta:
            print('voce venceu')
            break
            
    if tentativas == 0:
        print('voce perdeu a aplavra era' .format(palavra))
jogo()