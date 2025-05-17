## Programa para listagem de compras do mercado 
import os

list = []
def adcItm():
    list.append

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