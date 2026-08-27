print("=== MÉDIA DO ALUNO ===")

try:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: APROVADO")
    elif media >= 5:
        print("Situação: RECUPERAÇÃO")
    else:
        print("Situação: REPROVADO")

except ValueError:
    print("Erro: digite notas numéricas válidas.")
