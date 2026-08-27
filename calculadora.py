def calculadora():
    print("=== CALCULADORA ===")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Escolha uma operação: ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = num1 + num2
        elif opcao == "2":
            resultado = num1 - num2
        elif opcao == "3":
            resultado = num1 * num2
        elif opcao == "4":
            if num2 == 0:
                print("Erro: não é possível dividir por zero.")
                return
            resultado = num1 / num2
        else:
            print("Opção inválida.")
            return

        print(f"Resultado: {resultado:g}")

    except ValueError:
        print("Erro: digite números válidos.")


if __name__ == "__main__":
    calculadora()
