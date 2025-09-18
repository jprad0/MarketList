## Programa para listagem de compras do mercado 
import os



# adicionar um preço ficticio 


# Tambem realizar a criação de um sistema de saldo para assim efetuar compras



name = []
quantity = []
price = []


def adcItm():
    os.system("cls" if os.name == "nt" else "clear")
    print("================================")
    print("|   DIGITE O ITEM PARA LISTA   |")
    print("================================")
    adicionar = input("> ")
    name.append(adicionar)
    adcQ = int(input("Digite a quantidade> "))
    quantity.append(adcQ)
    adcPrice = float(input("Digite o preço: $"))
    price.append(adcPrice)
    
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
    for nome, qtd, prc in zip(name,quantity,price):
            print(f"{nome}: {qtd} : ${prc*qtd}")
            print("============================") 
    voltar = int (input("Voltar para o menu (1), (2) para somar compras ou 3 para sair! "))
    if voltar == 1:
        MenuInterativo()
    elif voltar == 2:
        somaTotal()
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
        
def somaTotal():
    os.system("cls" if os.name == "nt" else "clear")
    total = 0
    print("============================")
    print("|         TOTAL            |")
    print("============================")
    for qtd, prc in zip(quantity,price):
        total += prc * qtd
    print(f"TOTAL : ${total}")
    print("============================") 
    voltar = int (input("Voltar para o menu (1), (2) para somar compras ou 3 para sair! "))
    if voltar == 1:
        MenuInterativo()
    elif voltar == 3:
        print("obrigado por participar do projeto!")
    else:
        print("Opção inválida, retornando à lista.")
        showlist()
    
        
      
    
def removerItem():
    os.system("cls" if os.name == "nt" else "clear")
    print("============================")
    print("|    REMOVER UM ITEM       |")
    print("============================")
    for i, nome in enumerate(name):
        print(f"{i + 1}. {nome} ({quantity[i]})")
    try:
        indice = int(input("Digite o número do item para remover: ")) - 1
        if 0 <= indice < len(name):
            name.pop(indice)
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