def quiz():
    perguntas = {
        "I ____ speak English": "could",
        "I ____ run very fast.": "could",
        "You ____ work 7 days per week": "could",
        "You ____ play the piano.":"could",
        "He ____ understand England":"could",
        "It ___ happen with you too.":"can",
        "My sister ___ sing":"can't",
        "We ___ see very well at night.":"can't",
        "Anyone ___ make this wrong":"can",
        "My sister ___ dance with you.":"can",
        "He may not ___ come next week":"be",
        "I haven’t ____ sleep well recently":"been able to",
        "Are you going ____ to sell this old car?":"to be able ",
        "You should ____ do that in less than an hour":"be able to ",
        "They have ____ come here every day":"been able to",
    }
    desafios = {
        "imite um animal por 15 segundos ",
        "recite o alfabeto ao comtrario o mais rapido possivel",
        "coma uma fatia de limão sem fazer careta",
        "tente equilibrar um objeto com o dedo por 15 segundos"
    }

    pontuacao = 0
    for pergunta, resposta in perguntas.items():
        resposta_usuario = input(pergunta + " ").lower()
        if resposta_usuario == resposta:
            print("Correto!")
            pontuacao += 1
        else:
            print("Errado! A resposta correta é {}.".format(resposta))
            print("faça um desafio!")
            print(desafios.pop())

    print("Sua pontuação final é {} .".format(pontuacao))

quiz()