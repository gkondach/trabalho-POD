from RPG.Personagem import Personagem
from RPG.Arena import Arena
from RPG.Habilidade import Habilidade
from RPG.Classe import Classe
import random


def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis para o jogador.
    """
    print("\n==== MENU ====")
    print("1. Combate entre dois personagens")
    print("2. Combate entre múltiplos personagens (FreeForAll)")
    print("0. Sair")

def escolher_metodo(arena, personagens, limite):
    """
    Permite ao usuário gerenciar os personagens da arena antes do combate.

    Args:
        arena (Arena): Instância da arena onde os personagens serão adicionados ou removidos.
        personagens (list): Lista de personagens disponíveis para seleção.
        limite (int): Número máximo de personagens permitidos na arena.

    Returns:
        bool: True se o usuário iniciar o combate, False caso contrário.
    """
    adicionando = True
    while adicionando:
        print("\nComo deseja gerenciar os personagens?")
        print("1. Adicionar apenas um personagem")
        print("2. Remover um personagem")
        print("0. Iniciar combate")
        metodo = input("Escolha uma opção: ")

        if metodo == "1":
            if len(arena.personagens) >= limite:
                print("Limite de personagens atingido para este modo de combate.")
                continue
            sucesso = arena.adicionar_personagem(personagens)
            if not sucesso:
                print("[ERRO] Falha ao adicionar personagem.")
            else:
                print("1 personagem adicionado.")

        elif metodo == "2":
            if not arena.personagens:
                print("Nenhum personagem para remover.")
                continue
            print("\nPersonagens na arena:")
            for i, p in enumerate(arena.personagens):
                print(f"[{i}] {p.nome} - Classe: {p.classe.nome}")
            try:
                idx = int(input("Digite o número do personagem que deseja remover: "))
                if 0 <= idx < len(arena.personagens):
                    removido = arena.personagens.pop(idx)
                    print(f"Personagem {removido.nome} removido da arena.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Entrada inválida.")

        elif metodo == "0":
            if len(arena.personagens) < 2:
                print("É necessário pelo menos 2 personagens para iniciar o combate.")
            else:
                return True

        else:
            print("Opção inválida.")
    return False

def combate_duplo(personagens):
    """
    Inicia um combate entre dois personagens escolhidos pelo usuário.

    Args:
        personagens (list): Lista de personagens disponíveis.
    """
    if len(personagens) < 2:
        print("É necessário ao menos dois personagens para o combate.")
        return
    arena = Arena()
    sucesso = escolher_metodo(arena, personagens, 2)
    if not sucesso:
        return
    vencedor = arena.combate()
    if vencedor:
        print(f"\nVencedor: {vencedor.nome}")


def combate_free_for_all(personagens):
    """
    Inicia um combate entre múltiplos personagens (modo todos contra todos).

    Args:
        personagens (list): Lista de personagens disponíveis.
    """
    arena = Arena()
    sucesso = escolher_metodo(arena, personagens, len(personagens))
    if not sucesso:
        return
    vencedor = arena.combate()
    if vencedor:
        print(f"\nVencedor: {vencedor.nome}")
    else:
        print("Sem vencedores.")

def main():
    """
    Função principal do programa. Carrega os personagens a partir do arquivo de configuração
    e exibe o menu de interação com o usuário.
    """
    caminho_config = "config.md"
    with open("erros.md", "w", encoding="utf-8") as f:
        f.write("# Registro de Erros\n")
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
