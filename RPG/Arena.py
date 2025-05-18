import random
from RPG.Dado import D20
from RPG.Personagem import Personagem
from RPG.Classe import Guerreiro, Mago, Ladino
from RPG.Habilidade import Habilidade
import os

class Arena:
    """
    Classe que representa uma arena de combate onde personagens podem ser adicionados, removidos
    e batalhar entre si até restar um único vencedor.
    """
    def __init__(self):
        """
        Inicializa a arena com uma lista vazia de personagens.
        """
        self.personagens = []

    def adicionar_personagem(self, lista_personagens):
        """
        Permite ao usuário escolher um personagem de uma lista para adicionar à arena.
        Gera uma cópia independente do personagem escolhido.

        Parâmetros:
            lista_personagens (list): Lista de objetos Personagem disponíveis.

        Retorna:
            bool: True se o personagem foi adicionado com sucesso, False caso contrário.
        """

        print("\nEscolha um personagem para adicionar à arena:")
        for idx, p in enumerate(lista_personagens):
            print(f"[{idx}] {p.nome} - Classe: {p.classe.nome}")

        try:
            escolha = int(input("Digite o número correspondente ao personagem: "))
            personagem_base = lista_personagens[escolha]
        except (ValueError, IndexError):
            with open("erros.md", "a", encoding="utf-8") as f:
                f.write("[ERRO] Escolha inválida de personagem para adicionar à arena.\n")
            return False        
        #Gera uma cópia independente do personagem, para não alterar pv e inventario do original
        personagem_novo = Personagem(                                   
            nome=personagem_base.nome,
            classe=type(personagem_base.classe)(),
            inventario=[type(h)() for h in personagem_base.inventario]
        )
        # Verifica se o personagem já está na arena
        if personagem_novo not in self.personagens:
            self.personagens.append(personagem_novo)
            return True
        else:
            with open("erros.md", "a", encoding="utf-8") as f:
                f.write(f"[ERRO] {personagem_base.nome}: já inserido na arena.\n")
            return False

    def remover_personagem(self, personagem):
        """
        Remove um personagem da arena, se ele estiver presente.

        Parâmetros:
            personagem (Personagem): O personagem a ser removido.
        """
        if personagem in self.personagens:
            self.personagens.remove(personagem)

    def combate(self):
        """
        Executa o combate entre os personagens adicionados à arena. Cada personagem ataca em turnos,
        e o combate continua até que reste apenas um personagem vivo. Gera um relatório do combate
        em um arquivo markdown.

        Retorna:
            Personagem: O personagem vencedor do combate, ou None se o combate não puder ocorrer.
        """
        if len(self.personagens) < 2:
            erro_msg = "Numero de Combatentes insuficientes."
            print(erro_msg)
            self.registrar_erro(erro_msg)
            return None

        combatentes = self.personagens[:]  # Cria uma cópia da lista de personagens
        dado_d20 = D20()  # Instancia um dado de 20 lados
        log = []  # Lista para armazenar o registro do combate
        turno = 1  # Contador de turnos

        # O combate prossegue até que reste apenas um personagem vivo
        while len([p for p in combatentes if p.pontos_vida > 0]) > 1:
            vivos = [p for p in combatentes if p.pontos_vida > 0]  # Lista de personagens ainda vivos
            random.shuffle(vivos)  # Embaralha a ordem dos personagens no turno

            log.append(f"\n\n\n## Turno {turno}")  # Adiciona título do turno ao log

            for atacante in vivos:
                alvos = [p for p in vivos if p != atacante and p.pontos_vida > 0]  # Filtra alvos vivos que não sejam o próprio atacante
                if not alvos:
                    break
                alvo = random.choice(alvos)  # Escolhe um alvo aleatório

                try:
                    rolagem = dado_d20.jogar()  # Rola o D20
                    valor_ataque = rolagem + atacante.pontos_ataque  # Soma modificador de ataque

                    log.append(f"### {atacante.nome} ataca {alvo.nome}\n- Rolagem: {rolagem} + Ataque: {atacante.pontos_ataque} = {valor_ataque}")

                    if valor_ataque > alvo.pontos_defesa:
                        dano = atacante.atacar(alvo, alvos)  # Executa o ataque (pode ser simples, em área,bola de fogo ou cura)

                        if dano < 0:
                            # Habilidade de cura usada
                            log.append(f"- **Habilidade de cura usada!** {atacante.nome} recupera {-dano} pontos de vida. Vida atual: {atacante.pontos_vida}")
                        elif dano == 0:
                            # Ataque em área
                            log.append(f"- **Habilidade de ataque em área usada!** {atacante.nome} ataca e causa 6 de dano a todos os alvos.")
                            for alvo_area in alvos:
                                if alvo_area != atacante:
                                    log.append(f"- **Ataque em área!** {alvo_area.nome} sofre 6 de dano. Vida restante: {alvo_area.pontos_vida}")
                        elif dano > 20:
                            # Bola de fogo
                            log.append(f"- **Bola de fogo!** {alvo.nome} sofre 10 de dano. Vida restante: {alvo.pontos_vida}")
                        else:
                            # Ataque comum bem-sucedido
                            log.append(f"- **Ataque bem-sucedido!** {alvo.nome} sofre {dano} de dano. Vida restante: {alvo.pontos_vida}")
                    else:
                        # Defesa bem-sucedida
                        log.append(f"- {alvo.nome} defendeu o ataque com sucesso!")

                    # Atualiza a lista de vivos após o ataque
                    vivos = [p for p in combatentes if p.pontos_vida > 0]
                    # Mostra os alvos derrotados
                    for alvo_area in alvos:
                        if alvo_area.pontos_vida <= 0:
                            log.append(f"- **{alvo_area.nome} foi derrotado!**")
                except Exception as e:
                    erro_msg = f"Erro no turno {turno} entre {atacante.nome} e {alvo.nome}: {str(e)}"
                    print(erro_msg)
                    self.registrar_erro(erro_msg)

            turno += 1  # Avança para o próximo turno

        # Identifica o personagem vencedor
        vencedor = [p for p in combatentes if p.pontos_vida > 0][0]
        log.append(f"\n\n## Vencedor\n- {vencedor.nome}")

        # Salva o relatório do combate
        caminho_arquivo = "relatorio_combate.md"
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write("# Relatório de Combate\n")
            f.write("\n\n".join(log))

        print(f"\nO vencedor é {vencedor.nome}!")
        return vencedor  # Retorna o personagem vencedor
    

    def registrar_erro(self, mensagem):
        """
        Registra uma mensagem de erro no arquivo 'erros.md'. Se o arquivo não existir, ele será criado.

        Parâmetros:
            mensagem (str): A mensagem de erro a ser registrada.
        """
        caminho_erro = "erros.md"
        if not os.path.exists(caminho_erro):
            with open(caminho_erro, "w", encoding="utf-8") as f:
                f.write("# Registro de Erros\n")

        with open(caminho_erro, "a", encoding="utf-8") as f:
            f.write(mensagem + "\n")
