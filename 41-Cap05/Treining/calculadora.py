# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

import os

def soma(a, b):
    return a+b

def sub(a, b):
    return a-b 

def div(a, b):
    return a/b

def mult(a, b):
    return a*b

def pot(a, b):
    return a**b

saida = None
operador = None
while True:
    print("\n******************* Calculadora em Python *******************")
    print("Menu:\n0 - Sair\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Potencia\n-> ")
    menu = int(input())

    if menu != 0:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        if menu == 1:
            saida = soma(num1, num2)
            operador = "+"
        
        elif menu == 2:
            saida = sub(num1, num2)
            operador = "-"
            
        elif menu == 3:
            saida = div(num1, num2)
            operador = "/"
        
        elif menu == 4:
            saida = mult(num1, num2)
            operador = "*"
        
        elif menu == 5:
            saida = pot(num1, num2)
            operador = "^"
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{num1} {operador} {num2} = {saida}")
        input("\nPressione ENTER para continuar...")
        
            
    else:
        print("Saindo...")
        break
    