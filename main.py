from RPG.Personagem import Personagem
from RPG.Arena import Arena

import random


def exibir_menu():
    print("\n==== MENU ====")
    print("1. Combate entre dois personagens")
    print("2. Combate entre múltiplos personagens (FreeForAll)")
    print("0. Sair")


def combate_duplo(personagens):
    if len(personagens) < 2:
        print("É necessário ao menos dois personagens para o combate.")
        return
    arena = Arena()
    arena.adicionar_multipos_personagens(personagens, 2)
    vencedor = arena.combate()
    print(f"\nVencedor: {vencedor.nome}")


def combate_free_for_all(personagens):
    quantidade = int(input("Quantos personagens deseja adicionar à arena? "))
    if quantidade < 2:
        print("Deve haver pelo menos 2 personagens na arena.")
        return
    arena = Arena()
    arena.adicionar_multipos_personagens(personagens, quantidade)
    vencedor = arena.combate()
    if vencedor is None:
        print("Sem vencedores.")
    else:        
        print(f"\nVencedor: {vencedor.nome}")


def main():
    caminho_config = "config.md"
    try:
        personagens = Personagem.carregar_personagens(caminho_config)
    except FileNotFoundError as e:
        print(e)
        return

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            combate_duplo(personagens)
        elif opcao == "2":
            combate_free_for_all(personagens)
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
