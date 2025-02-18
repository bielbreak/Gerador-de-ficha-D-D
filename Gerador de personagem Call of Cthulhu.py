import random

# Definir as profissões disponíveis
profissoes = ["Detetive", "Médico", "Cientista", "Historiador", "Professor", "Soldado", "Escritor", "Policial"]

# Função para gerar os atributos de um personagem
def gerar_atributos():
    atributos = {
        "Força (STR)": random.randint(30, 80),
        "Constituição (CON)": random.randint(30, 80),
        "Tamanho (SIZ)": random.randint(30, 80),
        "Inteligência (INT)": random.randint(50, 99),
        "Poder (POW)": random.randint(30, 80),
        "Aparência (APP)": random.randint(30, 80),
        "Educação (EDU)": random.randint(50, 99),
        "Destreza (DEX)": random.randint(30, 80),
        "Lucky (LUC)": random.randint(30, 80)
    }

    # Calcular pontos de vida (HP) e pontos de sanidade (SAN)
    hp = (atributos["Constituição (CON)"] + atributos["Tamanho (SIZ)"]) // 10
    sanidade = atributos["Poder (POW)"] * 5  # SAN = POW x 5

    return atributos, hp, sanidade

# Função para gerar um personagem
def gerar_personagem():
    nome = input("Digite o nome do personagem: ")

    # Gerar atributos e pontos
    atributos, hp, sanidade = gerar_atributos()

    # Escolher uma profissão aleatoriamente
    profissao = random.choice(profissoes)

    # Exibir o personagem gerado
    print("\nPersonagem Gerado:")
    print(f"Nome: {nome}")
    print(f"Profissão: {profissao}")

    print("\nAtributos:")
    for atributo, valor in atributos.items():
        print(f"{atributo}: {valor}")

    print(f"\nPontos de Vida (HP): {hp}")
    print(f"Pontos de Sanidade (SAN): {sanidade}")

# Função principal
def main():
    while True:
        print("\nGerador de Personagem para Call of Cthulhu")
        opcao = input("\nDeseja gerar um personagem? (s/n): ").lower()

        if opcao == 's':
            gerar_personagem()
        elif opcao == 'n':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()
