def soma():
    x = float(input('primero numero: '))
    y = float(input('segundo numero: '))
    print('soma: ', x + y)


def subtrair():
    x = float(input('primeiro numero: '))
    y = float(input('segundo numero: '))
    print('subtracao: ', x - y)


def divisao():
    x = float(input('primero numero: '))
    y = float(input('segundo numero: '))
    print('divisao: ', x / y)


def multiplicacao():
    x = float(input('primero numero: '))
    y = float(input('segundo numero: '))
    print('multiplicacao: ', x * y)


def potencia():
    x = float(input('primero numero: '))
    y = float(input('numero elevado: '))
    print('potencia: ', x ** y)


opcao = 1

while opcao:
    print('1. soma')
    print('2. subtrair')
    print('3. divisao')
    print('4. multiplicacao')
    print('5. potencia')

    opcao = int(input('opcao: '))

    if opcao == 1:
        soma()
    if opcao == 2:
        subtrair()
    if opcao == 3:
        divisao()
    if opcao == 4:
        multiplicacao()
    if opcao == 5:
        potencia()
