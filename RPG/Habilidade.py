class Habilidade:
    def __init__(self, nome, descricao, pontos_ataque):
        self.nome = nome
        self.descricao = descricao
        self.pontos_ataque = pontos_ataque

    def usar(self):
        return self.pontos_ataque

    def __str__(self):
        return f"{self.nome} ({self.descricao}) - Ataque: {self.pontos_ataque}"

    def __repr__(self):
        return f"Habilidade('{self.nome}', '{self.descricao}', {self.pontos_ataque})"


class BolaDeFogo(Habilidade):
    def __init__(self):
        super().__init__("BolaDeFogo", "Uma bola de fogo que causa dano em área.", 10)

    def usar(self):
        return 10


class Cura(Habilidade):
    def __init__(self):
        super().__init__("Cura", "Uma cura que recupera 10 pontos de vida.", -10)

    def usar(self):
        return -10  # Valor negativo indica cura


class TiroDeArco(Habilidade):
    def __init__(self):
        super().__init__("Tiro de Arco", "Um tiro de arco que causa dano em área.", 6)

    def usar(self):
        return 6