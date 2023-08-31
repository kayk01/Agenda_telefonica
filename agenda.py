agenda = []

def inserir_contato():
    nome = input("Digite o nome do contato: ")
    numero = input("Digite o número de telefone do contato: ")
    contato = {"nome": nome, "numero": numero}
    agenda.append(contato)
    print("Contato adicionado com sucesso!")

def exibir_contatos():
    if len(agenda) == 0:
        print("A agenda está vazia.")
    else:
        print("Lista de contatos:")
        for idx, contato in enumerate(agenda, start=1):
            print(f"{idx}. Nome: {contato['nome']}, Número: {contato['numero']}")

def editar_contato():
    exibir_contatos()
    indice = int(input("Digite o número do contato que deseja editar: ")) - 1
    if 0 <= indice < len(agenda):
        novo_nome = input("Digite o novo nome do contato: ")
        novo_numero = input("Digite o novo número de telefone do contato: ")
        agenda[indice]["nome"] = novo_nome
        agenda[indice]["numero"] = novo_numero
        print("Contato editado com sucesso!")
    else:
        print("Índice inválido!")

def remover_contato():
    exibir_contatos()
    indice = int(input("Digite o número do contato que deseja remover: ")) - 1
    if 0 <= indice < len(agenda):
        contato_removido = agenda.pop(indice)
        print(f"Contato {contato_removido['nome']} removido com sucesso!")
    else:
        print("Índice inválido!")

while True:
    print("\nAgenda Telefônica")
    print("1. Inserir novo contato")
    print("2. Exibir lista de contatos")
    print("3. Editar um contato")
    print("4. Remover um contato")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        inserir_contato()
    elif opcao == "2":
        exibir_contatos()
    elif opcao == "3":
        editar_contato()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        print("Saindo da agenda telefônica.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
