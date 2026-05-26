def subtrair():
    n1 = int(input("Digite o primeiro número da subtração: "))
    n2 = int(input("Digite o segundo número da subtração: "))
    sub = n1 - n2
    print(n1," - ",n2," = ",sub)

opcao = 0
n1 = 0 
n2 = 0 

opcao = int(input("Sistema de calculadora!\nDigite 1 para somar\nDigite 2 para subtrair\nDigite 3 para multiplicar\nDigite 4 para dividir"))

if opcao == 1:
    n1 = int(input("Digite o primeiro número da soma: "))
    n2 = int(input("Digite o segundo número da soma: "))
    soma = n1 + n2
    print(n1," +1 ",n2," = ",soma)
elif opcao == 2:
    subtrair()