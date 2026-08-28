print("=== LISTA DE NOMES ===")

nomes = ["Eduardo", "Nicole", "Yasmim", "Ana", "Gabriel"]

print("Digite 5 nomes:")

for i in range(5):
    nome = input(f"{i + 1}º nome: ").strip()
    if nome:
        nomes.append(nome)

print("\n=== NOMES CADASTRADOS ===")

for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")

print(f"\nTotal de nomes: {len(nomes)}")
