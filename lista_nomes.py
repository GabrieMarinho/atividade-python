nomes = ["Gabriel", "Lucas", "Matheus", "Pedro", "Rafael"]

while True:
    print("\n===== MENU =====")
    print("1 - Ver nomes")
    print("2 - Pesquisar nome")
    print("3 - Ver quantidade")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nNomes cadastrados:")

        for i, nome in enumerate(nomes, start=1):
            print(f"{i}. {nome}")

    elif opcao == "2":
        nome_procurado = input("\nDigite o nome: ")

        encontrado = False

        for nome in nomes:
            if nome.lower() == nome_procurado.lower():
                encontrado = True
                break

        if encontrado:
            print("Nome encontrado na lista!")
        else:
            print("Nome não encontrado.")

    elif opcao == "3":
        print(f"\nExistem {len(nomes)} nomes cadastrados.")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
