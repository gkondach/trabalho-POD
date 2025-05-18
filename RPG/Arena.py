import random
from RPG.Dado import D20
from RPG.Personagem import Personagem
from RPG.Classe import Guerreiro, Mago, Ladino
from RPG.Habilidade import Habilidade
import os

class Arena:
    def __init__(self):
        self.personagens = []

    def adicionar_personagem(self, lista_personagens):
        tentativas = 0
        while tentativas < 100:
            personagem_base = random.choice(lista_personagens)

            personagem_novo = Personagem(
                nome=personagem_base.nome,
                classe=type(personagem_base.classe)(),
                inventario=[type(h)() for h in personagem_base.inventario]
            )

            if personagem_novo not in self.personagens:
                self.personagens.append(personagem_novo)
                return True
            else:
                tentativas += 1

        with open("erros.md", "a", encoding="utf-8") as f:
            f.write(f"[ERRO] {personagem_base.nome}: já inserido na arena.\n")
        return False

    def adicionar_multipos_personagens(self, lista_personagens, quantidade):
        adicionados = []
        tentativas = 0

        while len(adicionados) < quantidade and tentativas < 200:
            personagem_base = random.choice(lista_personagens)

            personagem_novo = Personagem(
                nome=personagem_base.nome,
                classe=type(personagem_base.classe)(),
                inventario=[type(h)() for h in personagem_base.inventario]
            )

            if personagem_novo not in adicionados:
                adicionados.append(personagem_novo)
            else:
                with open("erros.md", "a", encoding="utf-8") as f:
                    f.write(f"[ERRO] {personagem_base.nome}: já inserido na arena.\n")
            tentativas += 1

        if len(adicionados) == quantidade:
            self.personagens.extend(adicionados)
        else:
            with open("erros.md", "a", encoding="utf-8") as f:
                f.write("[ERRO] Falha ao adicionar personagens únicos suficientes na arena.\n")
        def remover_personagem(self, personagem):
            if personagem in self.personagens:
                self.personagens.remove(personagem)

    def combate(self):
        if len(self.personagens) < 2:
            erro_msg = "Numero de Combatentes insuficientes."
            print(erro_msg)
            self.registrar_erro(erro_msg)
            return None

        combatentes = self.personagens[:]
        dado_d20 = D20()
        log = []
        turno = 1

        while len([p for p in combatentes if p.pontos_vida > 0]) > 1:
            vivos = [p for p in combatentes if p.pontos_vida > 0]
            random.shuffle(vivos)

            log.append(f"\n\n\n## Turno {turno}")

            for atacante in vivos:
                alvos = [p for p in vivos if p != atacante and p.pontos_vida > 0]
                if not alvos:
                    break
                alvo = random.choice(alvos)

                try:
                    rolagem = dado_d20.jogar()
                    valor_ataque = rolagem + atacante.pontos_ataque

                    log.append(f"### {atacante.nome} ataca {alvo.nome}\n- Rolagem: {rolagem} + Ataque: {atacante.pontos_ataque} = {valor_ataque}")

                    if valor_ataque > alvo.pontos_defesa:
                        dano = atacante.atacar(alvo)
                        if dano < 0:
                            log.append(f"- **Habilidade de cura usada!** {atacante.nome} recupera {-dano} pontos de vida. Vida atual: {atacante.pontos_vida}")
                        else:
                            log.append(f"- **Ataque bem-sucedido!** {alvo.nome} sofre {dano} de dano. Vida restante: {alvo.pontos_vida}")
                    else:
                        log.append(f"- {alvo.nome} defendeu o ataque com sucesso!")

                    if alvo.pontos_vida <= 0:
                        log.append(f"- **{alvo.nome} foi derrotado!**")
                except Exception as e:
                    erro_msg = f"Erro no turno {turno} entre {atacante.nome} e {alvo.nome}: {str(e)}"
                    print(erro_msg)
                    self.registrar_erro(erro_msg)

            turno += 1

        vencedor = [p for p in combatentes if p.pontos_vida > 0][0]
        log.append(f"\n\n\n## Vencedor\n- {vencedor.nome}")

        caminho_arquivo = "relatorio_combate.md"
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write("# Relatório de Combate\n")
            f.write("\n\n".join(log))

        print(f"\nO vencedor é {vencedor.nome}!")
        return vencedor
    

    def registrar_erro(self, mensagem):
        caminho_erro = "erros.md"
        if not os.path.exists(caminho_erro):
            with open(caminho_erro, "w", encoding="utf-8") as f:
                f.write("# Registro de Erros\n")

        with open(caminho_erro, "a", encoding="utf-8") as f:
            f.write(mensagem + "\n")
