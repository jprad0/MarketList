## Programa para listagem de compras do mercado 
import os

list = []
def adcItm():
    os.system("cls")
    print("================================")
    print("|   DIGITE O ITEM PARA LISTA   |")
    print("================================")
    adicionar = input("> ")
    list.append(adicionar)
    pergunta = input("Deseja adicionar mais alguma coisa?").upper()
    if pergunta == "SIM":
        adcItm()
    elif pergunta == "NAO" or "NÃO":
        MenuInterativo()
        
    


def MenuInterativo():
    os.system("cls")
    print("============================")
    print("|      MENU DE OPCOES      |")
    print("| 1. Adicionar item        |")
    print("| 2. Mostrar lista         |")
    print("| 3. remover item da lista |")
    print("| 4. para sair             |")
    print("============================")
    resposta = int(input("Digite a opção desejada: "))
    if resposta == 1:
        adcItm()
    


def iniciar():
    print("==================================")
    print("|       LISTA DE COMPRAS         |")
    print("==================================")
    start = input("Digite 'INICIAR' para começar> ").upper()
    if start == "INICIAR":
        MenuInterativo()
    else:
        os.system("cls")
        print("Opção invalida!")
        iniciar()
iniciar()