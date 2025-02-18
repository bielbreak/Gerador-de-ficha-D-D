import random

# Definir as raças e classes disponíveis
racas = ["Humano", "Elfo", "Anão", "Orc", "Halfling", "Meio-Elfo"]
classes = ["Guerreiro", "Mago", "Ladino", "Clérigo", "Bárbaro", "Arqueiro"]

# Função para gerar um personagem com atributos aleatórios
def gerar_personagem():
    nome = input("Digite o nome do personagem: ")

    # Gerar atributos de forma aleatória
    atributos = {
        "Força": random.randint(8, 18),
        "Destreza": random.randint(8, 18),
        "Inteligência": random.randint(8, 18),
        "Sabedoria": random.randint(8, 18),
        "Carisma": random.randint(8, 18),
        "Constituição": random.randint(8, 18)
    }

    # Escolher aleatoriamente a raça e a classe
    raca = random.choice(racas)
    classe = random.choice(classes)

    # Exibir o personagem gerado
    print("\nPersonagem Gerado:")
    print(f"Nome: {nome}")
    print(f"Raça: {raca}")
    print(f"Classe: {classe}")
    
    print("\nAtributos:")
    for atributo, valor in atributos.items():
        print(f"{atributo}: {valor}")

# Função principal
def main():
    while True:
        print("\nGerador de Personagem para RPG de Mesa")
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
