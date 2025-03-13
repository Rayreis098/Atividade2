
def linha():
    print('___________________________________')


while True: #estratégia de implementação com laço de repetção while true

    #Tratamento de erro
    try:
        linha()
        print('Bem vindos á calculadora de divisão!!!')
        linha()
        print()


        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

        conta = n1 / n2
    
    except ZeroDivisionError:
        linha()
        print('não é possível dividir nada por 0')
        linha()
    except ValueError:
        linha()
        print('por favor, digite apenas números inteiros')
        linha()

    else:
        print(f'{n1} dividido por {n2} é = {conta}')
        break
    
    

