import random
from RPG.Habilidade import BolaDeFogo, Cura, TiroDeArco
from RPG.Classe import Classe , Guerreiro, Mago, Ladino
from RPG.Dado import D4, D6, D8, D10, D12, D20
import os

class Personagem:

    """
    Classe que representa um personagem no jogo de RPG.

    Atributos:
    nome (str): Nome do personagem.
    classe (Classe): Classe do personagem (ex: Guerreiro, Mago).
    inventario (list): Lista de habilidades do personagem.

    Métodos:
    atacar(alvo): Realiza um ataque contra outro personagem.
    usar_habilidade(): Usa uma habilidade do inventário.
    """
    qntd_instancias = 0

    def __str__(self):
        """
        Retorna uma representação legível do personagem para exibição ao usuário.

        Retorna:
            str: Uma string no formato "Personagem: <nome>, Classe: <classe>".
        """
        return f"Personagem: {self.nome}, Classe: {self.classe.nome}"

    def __repr__(self):
        """
        Retorna uma representação oficial do objeto Personagem, útil para depuração.

        Retorna:
            str: Uma string no formato "<Personagem(nome=<nome>, classe=<classe>)>".
        """
        return f"<Personagem(nome={self.nome}, classe={self.classe.nome})>"

    def __eq__(self, other):
        """
        Compara dois objetos Personagem para verificar igualdade com base no nome e classe.

        Parâmetros:
            other (Personagem): Outro objeto Personagem a ser comparado.

        Retorna:
            bool: True se ambos os personagens tiverem o mesmo nome e classe, False caso contrário.
        """
        if isinstance(other, Personagem):
            return self.nome == other.nome and self.classe.__class__ == other.classe.__class__
        return False

    def __init__(self, nome, classe, inventario=None):
        """
        Inicializa um novo personagem com nome, classe e habilidades.

        Define os atributos iniciais com base na classe fornecida, incluindo pontos de vida,
        ataque, defesa e o dado de ataque. Aumenta o contador de instâncias da classe.

        Parâmetros:
        nome (str): Nome do personagem.
        classe (Classe): Objeto da classe que define os atributos do personagem.
        inventario (list[Habilidade]): Lista de habilidades disponíveis no inventário do personagem.
        """
        self.nome = nome
        self.classe = classe #deve ser uma instância de Guerreiro, Mago ou Ladino
        self.pontos_vida = classe.pontos_vida
        self.dado_de_ataque = classe.dado_de_ataque
        self.pontos_ataque = classe.pontos_ataque
        self.pontos_defesa = classe.pontos_defesa
        self.inventario = inventario if inventario else []
        Personagem.qntd_instancias += 1

    def atacar(self, alvo,alvos):
        """
        Realiza um ataque contra outro personagem, podendo usar uma habilidade ou o dado de ataque.

        Se o personagem possuir habilidades em seu inventário, existe uma chance de 50% de utilizar
        uma habilidade ao invés de realizar um ataque normal com o dado. Se for utilizado o ataque 
        padrão, o dano será definido pelo resultado do dado de ataque da classe, e os pontos de vida 
        do alvo serão reduzidos pelo valor do dano.

        Parâmetros:
        alvo (Personagem): O personagem que será atacado.
        alvos (list[Personagem]): Lista de possíveis alvos, usada em habilidades que podem atingir múltiplos.

        Retorna:
        int: O valor do dano causado ao alvo.
        """
        usar_habilidade = self.inventario and random.random() < 0.5
        if usar_habilidade:
            return self.usar_habilidade(alvo,alvos)
        else:
            dano = self.dado_de_ataque.jogar()
            alvo.pontos_vida -= dano
            return dano

    def usar_habilidade(self, alvo,alvos):
        """
        Utiliza uma habilidade do inventário contra um alvo.

        A habilidade é removida do inventário após o uso. Se a habilidade causar dano negativo,
        ela será considerada uma cura e afetará o próprio personagem ao invés do alvo. Caso
        contrário, o dano da habilidade descrito na classe habilidade correspondente será aplicado ao alvo.

        Parâmetros:
        alvo (Personagem): O personagem que seria alvo da habilidade.
        alvos (list[Personagem]): Lista de possíveis alvos (usada para habilidades em área, se aplicável).

        Retorna:
        int: O valor do dano (maior que 20 caso seja bola de fogo, 0 se for dano em area e negativo se for cura)
        """
        if not self.inventario:
            return self.atacar(alvo,alvos)

        habilidade = self.inventario.pop(0)
        dano = habilidade.usar()

        if isinstance(habilidade, Cura):
            self.pontos_vida += abs(dano)
        elif isinstance(habilidade, TiroDeArco):          
            dano = 0
            for alvo_area in alvos:
                if alvo_area != self:
                    alvo_area.pontos_vida -= 6
        elif isinstance(habilidade, BolaDeFogo):
            dano = 25
            alvo.pontos_vida -= 10
        else:
            alvo.pontos_vida -= dano

        return dano

    @staticmethod
    def carregar_personagens(caminho_arquivo):
        """
        Carrega personagens a partir de um arquivo de configuração em formato Markdown.

        O método lê o arquivo especificado e interpreta blocos de texto que representam personagens.
        Cada personagem deve conter seu nome, classe e lista de habilidades.
        Apenas classes válidas (Guerreiro, Mago, Ladino) e habilidades válidas (BolaDeFogo, Cura, Tiro de Arco)
        são aceitas. Erros de configuração são registrados no arquivo 'erros.md'.

        Parâmetros:
        caminho_arquivo (str): Caminho para o arquivo de configuração (ex: 'config.md').

        Retorna:
        list[Personagem]: Lista de objetos do tipo Personagem carregados com sucesso.

        Exceções:
        FileNotFoundError: Se o arquivo de configuração não for encontrado.

        Observações:
        - Erros de parsing (classe ou habilidade inválida, excesso de habilidades, etc.)
          são registrados com detalhes no arquivo 'erros.md', substituindo o conteúdo anterior.
        """
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

        if erros:
            with open("erros.md", 'w', encoding="utf-8") as log:
                for erro in erros:
                    log.write(erro + "\n")

        return personagens