from abc import ABC, abstractmethod
from RPG.Dado import D4, D6, D8, D10, D12 ,D20

class Classe(ABC):
    def __init__(self, nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades):
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.dado_de_ataque = dado_de_ataque  # Deve ser uma instância de Dado
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.limite_habilidades = limite_habilidades

    def __str__(self):
        return (
            f"Classe: {self.nome}\n"
            f"Vida: {self.pontos_vida}\n"
            f"Ataque: {self.pontos_ataque} + {self.dado_de_ataque}\n"
            f"Defesa: {self.pontos_defesa}\n"
            f"Limite de Habilidades: {self.limite_habilidades}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"'{self.nome}', {self.pontos_vida}, {repr(self.dado_de_ataque)}, "
            f"{self.pontos_ataque}, {self.pontos_defesa}, {self.limite_habilidades})"
        )

class Guerreiro(Classe):
    def __init__(self):
        nome = "Guerreiro"
        pontos_defesa = 8
        pontos_vida = 10 + (pontos_defesa * 5)
        dado_de_ataque = D12()
        pontos_ataque = 6
        limite_habilidades = 2
        super().__init__(nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)


class Mago(Classe):
    def __init__(self):
        nome = "Mago"
        pontos_defesa = 3
        pontos_vida = 8 + (pontos_defesa * 2)
        dado_de_ataque = D6()
        pontos_ataque = 10
        limite_habilidades = 5
        super().__init__(nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)


class Ladino(Classe):
    def __init__(self):
        nome = "Ladino"
        pontos_defesa = 5
        pontos_vida = 6 + (pontos_defesa * 3)
        dado_de_ataque = D8()
        pontos_ataque = 8
        limite_habilidades = 3
        super().__init__(nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)

