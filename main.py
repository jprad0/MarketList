## Programa para listagem de compras do mercado 
import os


nomes = []
quantity = []

def adcItm():
    os.system("cls" if os.name == "nt" else "clear")
    print("================================")
    print("|   DIGITE O ITEM PARA LISTA   |")
    print("================================")
    adicionar = input("> ")
    nomes.append(adicionar)
    adcQ = input("Digite a quantidade> ")
    quantity.append(adcQ)
    
    pergunta = input("Deseja adicionar mais alguma coisa? ").upper()
    if pergunta == "SIM":
        adcItm()
    elif pergunta in ["NAO", "NÃO"]:
        MenuInterativo()
    else:
        print("Opção inválida, retornando ao menu.")   
        MenuInterativo()
             
def showlist(): 
    os.system("cls" if os.name == "nt" else "clear")
    print("============================")
    print("|         Lista            |")
    print("============================")
    for nome, qtd in zip(nomes,quantity):
            print(f"{nome}: {qtd}")
            print("============================") 
    voltar = int (input("Voltar para o menu (1) ou 3 para sair! "))
    if voltar == 1:
        MenuInterativo()
    elif voltar == 3:
        print("obrigado por participar do projeto!")
    else:
        print("Opção inválida, retornando à lista.")
        showlist()
    


def MenuInterativo():
    os.system("cls" if os.name == "nt" else "clear")
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
    elif resposta == 2:
        showlist()
    elif resposta == 3:
        removerItem()
    elif resposta == 4:
        print("Encerrando o programa, Até Logo!")
    else:
        print("Opção inválida.")
        MenuInterativo()
    
def removerItem():
    os.system("cls" if os.name == "nt" else "clear")
    print("============================")
    print("|    REMOVER UM ITEM       |")
    print("============================")
    for i, nome in enumerate(nomes):
        print(f"{i + 1}. {nome} ({quantity[i]})")
    try:
        indice = int(input("Digite o número do item para remover: ")) - 1
        if 0 <= indice < len(nomes):
            nomes.pop(indice)
            quantity.pop(indice)
            print("Item removido com sucesso.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

    input("Pressione Enter para voltar ao menu.")
    MenuInterativo()
    


def iniciar():
    os.system("cls")
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