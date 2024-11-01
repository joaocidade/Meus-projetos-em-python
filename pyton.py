def menu():
    print('escolha uma opção: ')
    while True:
        print('1 - somar')
        print("2 - subtrair")
        print("3 - multiplicar")        
        print("4 - dividir")
    
def soma():
    n1 = float(input('digite o primeiro valor: '))
    n2 = float(input('digite o segundo valor: '))
    resultado1 = n1 + n2
    print(resultado1)

def subtrair():
    n1 = float(input('digite o primeiro valor: '))
    n2 = float(input('digite o segundo valor: '))
    resultado2 = n1 - n2
    print(resultado2)    

escolha = input('Escolha uma opção (1/2/3/4): ')
        
if escolha == '1':
    soma()
elif escolha == '2':
    subtrair()
else:
    print('Opção inválida')
    
menu()

