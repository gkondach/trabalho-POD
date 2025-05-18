import random
from RPG.Habilidade import BolaDeFogo, Cura, TiroDeArco
from RPG.Classe import Classe , Guerreiro, Mago, Ladino
from RPG.Dado import D4, D6, D8, D10, D12, D20
import os

class Personagem:
    qntd_instancias = 0

    def __str__(self):
        return f"Personagem: {self.nome}, Classe: {self.classe.nome}"

    def __repr__(self):
        return f"<Personagem(nome={self.nome}, classe={self.classe.nome})>"

    def __eq__(self, other):
        if isinstance(other, Personagem):
            return self.nome == other.nome and self.classe.__class__ == other.classe.__class__
        return False

    def __init__(self, nome, classe, inventario=None):
        self.nome = nome
        self.classe = classe
        self.pontos_vida = classe.pontos_vida
        self.dado_de_ataque = classe.dado_de_ataque
        self.pontos_ataque = classe.pontos_ataque
        self.pontos_defesa = classe.pontos_defesa
        self.inventario = inventario if inventario else []
        Personagem.qntd_instancias += 1

    def atacar(self, alvo):
        usar_habilidade = self.inventario and random.random() < 0.5
        if usar_habilidade:
            return self.usar_habilidade(alvo)
        else:
            dano = self.dado_de_ataque.jogar()
            alvo.pontos_vida -= dano
            return dano

    def usar_habilidade(self, alvo):
        if not self.inventario:
            return self.atacar(alvo)

        habilidade = self.inventario.pop(0)
        dano = habilidade.usar()

        if isinstance(habilidade, Cura):
            self.pontos_vida += abs(dano)
        else:
            alvo.pontos_vida -= dano

        return dano

    @staticmethod
    def carregar_personagens(caminho_arquivo):
        personagens = []
        erros = []

        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError("Arquivo de configuração não encontrado.")

        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        blocos = conteudo.split('### ')[1:]
        for bloco in blocos:
            linhas = bloco.strip().split('\n')
            nome = linhas[0].strip()

            classe = None
            habilidades = []
            habilidades_started = False

            for linha in linhas[1:]:
                linha = linha.strip()
                if linha.startswith('- **Classe**:'):
                    classe_str = linha.split(':', 1)[1].strip()
                    if classe_str == 'Guerreiro':
                        classe = Guerreiro()
                    elif classe_str == 'Mago':
                        classe = Mago()
                    elif classe_str == 'Ladino':
                        classe = Ladino()
                    else:
                        erros.append(f"[ERRO] {nome}: Classe inválida ({classe_str}).")
                        classe = None
                        break
                elif linha.startswith('- **Habilidades**:'):
                    habilidades_started = True
                elif linha.startswith('- ') and habilidades_started:
                    hab_nome = linha[2:].strip()
                    if hab_nome == 'BolaDeFogo':
                        habilidades.append(BolaDeFogo())
                    elif hab_nome == 'Cura':
                        habilidades.append(Cura())
                    elif hab_nome == 'Tiro de Arco':
                        habilidades.append(TiroDeArco())
                    else:
                        erros.append(f"[ERRO] {nome}: Habilidade inválida ({hab_nome}).")

            if not classe:
                erros.append(f"[ERRO] {nome}: Classe não encontrada.")
                continue

            if len(habilidades) > classe.limite_habilidades:
                erros.append(f"[ERRO] {nome}: Excedeu o limite de habilidades da classe {classe.nome}.")
                continue

            personagem = Personagem(nome, classe, habilidades)
            personagens.append(personagem)

        #achei que seria mais facil para correção se não apagasse os erros anteriores 
        if erros:
            with open("erros.md", 'w', encoding="utf-8") as log:
                for erro in erros:
                    log.write(erro + "\n")

        return personagens