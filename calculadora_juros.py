def juros_simples():
    simples = capital * tempo * (juros/100)
    print('R$',simples)
def juros_compostos():
    composto = capital *(1 + juros/100)**tempo
    print('R$',composto)

juros = float(input('digite o juros %/mes: '))
capital = float(input('digite o capital: '))
tempo = float(input('digite o tempo /mes: '))

print('escolha uma opção: ')
print('1 - juros simples')
print('2 - juros compostos')

escolha = int(input('escolha uma opção: '))

if escolha == 1:
    juros_simples()
else:
    juros_compostos()



