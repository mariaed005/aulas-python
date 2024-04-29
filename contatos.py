l1 = []


def menu_principal():
    print("Menu Principal")
    print("(C) Cadastrar")
    print("(L) Listar")
    print("(P) Procurar")
    print("(B) Backup em um arquivo")
    print( "(R) Restaurar de um arquivo")
    print("(S) Sair")
    opcao = (input().lower()[0]("Escolha sua opcao: "))
    return opcao

def cadastrar_contato():
    nome = input(("Informe seu nome:"))
    telefone = int(input("Informe seu telefone:"))
    email= input(("Informe seu email:"))
    peso = float(input("Informe seu peso:"))
    d = {"nome": nome, "telefone":telefone,  "email": email,"peso": peso}
    return d

def listar_contatos(lista_contato):
    indice = 0
    while indice <= len(lista_contato):
        contato = lista_contato
        print("Nome\t\tTelefone\t\tEmail\t\tPeso")
        print(f"{contato['nome']}\t\t{contato['telefone']}\t\t " +
            f"{contato['email']}f{contato['peso']}")

def procurar_contato(lista_contato):
    print("Procurar contato:")
    email = (("Informe o email para pesquisar:"))
    indice = 0
    while indice < len(lista_contato):
        contato = lista_contato
        if contato ["email"] == email:
            print("Nome\t\tTelefone\t\tEmail\t\tPeso")
            print(f"{contato['nome']}\t\t{contato['telefone']}\t\t " +
                f"{contato['email']}f{contato['peso']}")
            
            print("Menu de opções para contato")
            print("(R)emover o contato")
            print("(A)lterar o contato")
            print("(V)oltar para o menu principal")
            print("Por favor escolha sua opcao ==> ")
            opcao = input()
            if opcao == 'R':
                del lista_contato[indice]
            elif opcao == 'A':
                print("Alterar contato")
                print("Digite o nome completo do contato: ")
                nome = input()
                print("Informe o Telefone do contato: ")
                telefone = input()
                print("Informe o E-Mail do contato: ")
                email = input()
                print("Informe o Peso do contato: ")
                peso = float(input())
                d = {"nome": nome, "telefone": telefone, "email": email, "peso": peso}
                lista_contato[indice] = d

        indice = indice + 1
    
executando = True
while executando:
    print("Programa de gestão de contatos")
    letra = menu_principal()
    if letra == 'C':
        cadastrar_contato()
    elif letra == 'L':
        listar_contatos()
    elif letra == 'S':
        print("Até Breve")
        executando = False