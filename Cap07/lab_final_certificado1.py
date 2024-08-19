import random
import re
import os
frutas = ["banana", "melancia", "maça", "tomate"]
objetos = ["celular", "mesa", "cadeira", "parafusadeira", "unhex"]
ufpi = ["professor", "discente", "laboratorio", "maconheiro", "aluno", "restaurante", "biblioteca"]

while True:
    erros = 0
    acertos = 0
    letras_tentadas = []
    tentativa = None

    os.system("cls")

    print("\n\n-----Bem-Vindo ao jogo da forca!!!-----\n\n")
    
    print("Escolha um tema: ")
    menu1 = int(input("1 - Frutas\n2 - Objetos\n3 - Tem na UFPI\n4 - Sair\n->"))
    if menu1 == 1:
        fruta = random.randint(0, (len(frutas)-1))
        palavra = frutas[fruta]
        tema_escolhido = "Frutas"
        
    elif menu1 == 2:
        objeto = random.randint(0, (len(objetos)-1))
        palavra = objetos[objeto]
        tema_escolhido = "Objetos"

    elif menu1 == 3:
        ufpi_escolhida = random.randint(0, (len(ufpi)-1))
        palavra = ufpi[ufpi_escolhida]
        tema_escolhido = "Tem na UFPI"

    elif menu1 == 4:
        print("Saindo...")
        break
    while True:
        os.system("cls")
                
        print("-------------------------------------------")
        print("\n\n-------O JOGO VAI COMEÇAR, BOA SORTE-------\n\n")
        print("-------------------------------------------")
        print(f"Tema escolhido: {tema_escolhido}")
        
        
        print("Que comecem os jogos!!!\n\n")
        
        for i in palavra:
            if i in letras_tentadas:
                print(i, end=' ')
            elif i == " ":
                print(" ", end=' ')
            else:
                print("_", end=' ')
            
        if erros == 0:
            print('''
                  _____
                  |
                  |
                  |
                  |
                  |
                  ''')
        elif erros == 1:
            print('''
                  _____
                  |   O
                  |
                  |
                  |
                  |
                  ''')
        elif erros == 2:
            print('''
                  _____
                  |   O
                  |   |
                  |
                  |
                  |
                  ''')
        elif erros == 3:
            print('''
                  _____
                  |   O
                  |   |-
                  |
                  |
                  |
                  ''')
        elif erros == 4:
            print('''
                  _____
                  |   O
                  |  -|-
                  |
                  |
                  |
                  ''')
        elif erros == 5:
            print('''
                  _____
                  |   O
                  |  -|-
                  |  /
                  |
                  |
                  ''')
        elif erros == 6:
            print('''
                  _____
                  |   O
                  |  -|-
                  |  /|
                  |
                  |
                  ''')
            
            print("Você perdeu T.T\n\n")
            input("Aperte em qualquer coisa para sair...\n")
            break
            
        print("\n\n\n")
        print("Letras Tentadas: ", end='')
        for j in letras_tentadas:
            print(j, end=' ')
            
        print("\n")
        
        if acertos == len(palavra):
            print('\n\n----------- UAU GÊNIO VOCE GANHOU ----------------\n\n')
            break
            
        tentativa = str(input("Tenta uma letra: "))
    
        if tentativa not in palavra or tentativa in letras_tentadas:
            erros += 1
        else:
            acertos += 1
        
        letras_tentadas.append(tentativa)

            
        
        