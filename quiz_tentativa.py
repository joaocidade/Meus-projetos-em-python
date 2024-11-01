def quiz():
    pergunta = "Qual é a capital da França?"
    opcoes = ["a) Paris", "b) Madrid", "c) Londres", "d) POA"]
    resposta_certa = 'd'

    print(pergunta)
    for opcao in opcoes:
        print(opcao)

    resposta = input("Digite a letra da sua resposta: ").strip().lower()

    if resposta == resposta_certa:
        print("Correto! Paris é a capital da França.")
    elif resposta in [opcao[0] for opcao in opcoes]:
        print("Incorreto. A resposta correta é a) Paris.")
    else:
        print("Resposta inválida. Por favor, digite a letra correspondente a uma das opções.")

quiz()
