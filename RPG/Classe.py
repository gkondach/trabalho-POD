from abc import ABC, abstractmethod
from RPG.Dado import D4, D6, D8, D10, D12 ,D20

class Classe(ABC):
    """
    Classe abstrata que define os atributos e comportamentos comuns a todas as classes de personagens.

    Atributos:
        nome (str): Nome da classe.
        pontos_vida (int): Pontos de vida iniciais.
        dado_de_ataque (Dado): Instância de um dado usado nos ataques.
        pontos_ataque (int): Modificador fixo de ataque.
        pontos_defesa (int): Pontos de defesa do personagem.
        limite_habilidades (int): Número máximo de habilidades que a classe pode ter.
    """
    def __init__(self, nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades):
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.dado_de_ataque = dado_de_ataque  # Deve ser uma instância de Dado
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.limite_habilidades = limite_habilidades

    def __str__(self):
        """Retorna uma string formatada com as características da classe."""
        return (
            f"Classe: {self.nome}\n"
            f"Vida: {self.pontos_vida}\n"
            f"Ataque: {self.pontos_ataque} + {self.dado_de_ataque}\n"
            f"Defesa: {self.pontos_defesa}\n"
            f"Limite de Habilidades: {self.limite_habilidades}"
        )

    def __repr__(self):
        """Retorna uma representação de depuração da classe."""
        return (
            f"{self.__class__.__name__}("
            f"'{self.nome}', {self.pontos_vida}, {repr(self.dado_de_ataque)}, "
            f"{self.pontos_ataque}, {self.pontos_defesa}, {self.limite_habilidades})"
        )


class Guerreiro(Classe):
    """
    Classe concreta que representa o Guerreiro. Alta vida e defesa, ataque moderado.
    """
    def __init__(self):
        nome = "Guerreiro"
        pontos_defesa = 8  # Alta defesa
        pontos_vida = 10 + (pontos_defesa * 5)  # Vida baseada na defesa
        dado_de_ataque = D12()  # Dado de ataque poderoso
        pontos_ataque = 6  # Ataque base
        limite_habilidades = 2  # Poucas habilidades
        super().__init__(nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)


class Mago(Classe):
    """
    Classe concreta que representa o Mago. Alto ataque, baixa defesa e vida.
    """
    def __init__(self):
        nome = "Mago"
        pontos_defesa = 3  # Defesa baixa
        pontos_vida = 8 + (pontos_defesa * 2)  # Vida baixa
        dado_de_ataque = D6()  # Dado de ataque fraco
        pontos_ataque = 10  # Alto ataque base
        limite_habilidades = 5  # Muitas habilidades
        super().__init__(nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)


class Ladino(Classe):
    """
    Classe concreta que representa o Ladino. Equilibrado em ataque, defesa e habilidades.
    """
    def __init__(self):
        nome = "Ladino"
        pontos_defesa = 5  # Defesa média
        pontos_vida = 6 + (pontos_defesa * 3)  # Vida moderada
        dado_de_ataque = D8()  # Dado de ataque médio
        pontos_ataque = 8  # Ataque razoável
        limite_habilidades = 3  # Número equilibrado de habilidades
        super().__init__(nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)

