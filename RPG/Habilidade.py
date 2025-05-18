class Habilidade:
    """
    Classe base para representar uma habilidade em combate.

    Atributos:
        nome (str): Nome da habilidade.
        descricao (str): Descrição da habilidade.
        pontos_ataque (int): Valor numérico de ataque ou cura da habilidade.
    """
    def __init__(self, nome, descricao, pontos_ataque):
        self.nome = nome
        self.descricao = descricao
        self.pontos_ataque = pontos_ataque

    def usar(self):
        """
        Executa a habilidade.

        Retorna:
            int: O valor de ataque ou cura da habilidade.
        """
        return self.pontos_ataque

    def __str__(self):
        """Retorna uma representação legível da habilidade."""
        return f"{self.nome} ({self.descricao}) - Ataque: {self.pontos_ataque}"

    def __repr__(self):
        """Retorna uma representação formal da habilidade."""
        return f"Habilidade('{self.nome}', '{self.descricao}', {self.pontos_ataque})"


class BolaDeFogo(Habilidade):
    """
    Habilidade especial que causa 10 de dano em área.
    """
    def __init__(self):
        super().__init__("BolaDeFogo", "Uma bola de fogo que causa dano em área.", 10)

    def usar(self):
        """
        Executa a habilidade Bola de Fogo.

        Retorna:
            int: Valor fixo de dano (10).
        """
        return 10


class Cura(Habilidade):
    """
    Habilidade que recupera 10 pontos de vida do usuário.
    """
    def __init__(self):
        super().__init__("Cura", "Uma cura que recupera 10 pontos de vida.", -10)

    def usar(self):
        """
        Executa a habilidade de cura.

        Retorna:
            int: Valor fixo de cura (-10), indicando recuperação de vida.
        """
        return -10  # Valor negativo indica cura


class TiroDeArco(Habilidade):
    """
    Habilidade de ataque em área que causa 6 de dano a múltiplos inimigos.
    """
    def __init__(self):
        super().__init__("Tiro de Arco", "Um tiro de arco que causa dano em área.", 6)

    def usar(self):
        """
        Executa a habilidade Tiro de Arco.

        Retorna:
            int: Valor fixo de dano (6).
        """
        return 6
