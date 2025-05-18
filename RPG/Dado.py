from abc import ABC, abstractmethod
import random
from functools import total_ordering

@total_ordering
class Dado(ABC):
    """
    Classe abstrata que representa um dado genérico com um número definido de lados.

    Fornece métodos de comparação baseados no número de lados, além de obrigar a implementação
    do método `jogar()` nas subclasses.

    Atributos:
    lados (int): Número de lados do dado.
    """

    def __init__(self, lados):
        """
        Inicializa um dado com a quantidade especificada de lados.

        Parâmetros:
        lados (int): Número de lados do dado.
        """
        self.lados = lados

    @abstractmethod
    def jogar(self):
        """
        Método abstrato para simular o lançamento do dado.

        Deve ser implementado pelas subclasses para retornar um valor aleatório
        entre 1 e o número de lados.
        """
        pass

    def __str__(self):
        """
        Retorna uma representação legível do dado.

        Retorna:
        str: Representação como "Dado de X lados".
        """
        return f"Dado de {self.lados} lados"

    def __repr__(self):
        """
        Retorna uma representação oficial do dado, útil para debug.

        Retorna:
        str: Nome da classe com parênteses.
        """
        return f"{self.__class__.__name__}()"

    def __eq__(self, other):
        """
        Compara se dois dados têm o mesmo número de lados.

        Parâmetros:
        other (Dado): Outro dado a ser comparado.

        Retorna:
        bool: True se os dados têm o mesmo número de lados, False caso contrário.
        """
        if isinstance(other, Dado):
            return self.lados == other.lados
        return NotImplemented

    def __lt__(self, other):
        """
        Compara se este dado tem menos lados que outro.

        Parâmetros:
        other (Dado): Outro dado a ser comparado.

        Retorna:
        bool: True se este dado tiver menos lados.
        """
        if isinstance(other, Dado):
            return self.lados < other.lados
        return NotImplemented


# Subclasses específicas
class D4(Dado):
    """
    Representa um dado de 4 lados (D4).

    Herda de Dado e implementa o método `jogar` para retornar um valor aleatório entre 1 e 4.
    """
    def __init__(self):
        """
        Inicializa o dado com 4 lados.
        """
        super().__init__(4)

    def jogar(self):
        """
        Simula o lançamento do dado.

        Retorna:
        int: Valor aleatório entre 1 e 4.
        """
        return random.randint(1, self.lados)

class D6(Dado):
    """
    Representa um dado de 6 lados (D6).

    Herda de Dado e implementa o método `jogar` para retornar um valor aleatório entre 1 e 6.
    """

    def __init__(self):
        """
        Inicializa o dado com 6 lados.
        """
        super().__init__(6)

    def jogar(self):
        """
        Simula o lançamento do dado.

        Retorna:
        int: Valor aleatório entre 1 e 6.
        """
        return random.randint(1, self.lados)

class D8(Dado):
    """
    Representa um dado de 8 lados (D8).

    Herda de Dado e implementa o método `jogar` para retornar um valor aleatório entre 1 e 8.
    """
     
    def __init__(self):
        """
        Inicializa o dado com 8 lados.
        """
        super().__init__(8)

    def jogar(self):
        """
        Simula o lançamento do dado.

        Retorna:
        int: Valor aleatório entre 1 e 8.
        """
        return random.randint(1, self.lados)

class D10(Dado):
    """
    Representa um dado de 10 lados (D10).

    Herda de Dado e implementa o método `jogar` para retornar um valor aleatório entre 1 e 10.
    """
    def __init__(self):
        """
        Inicializa o dado com 10 lados.
        """
        super().__init__(10)

    def jogar(self):
        """
        Simula o lançamento do dado.

        Retorna:
        int: Valor aleatório entre 1 e 10.
        """
        return random.randint(1, self.lados)

class D12(Dado):
    """
    Representa um dado de 12 lados (D12).

    Herda de Dado e implementa o método `jogar` para retornar um valor aleatório entre 1 e 12.
    """
    def __init__(self):
        """
        Inicializa o dado com 12 lados.
        """
        super().__init__(12)

    def jogar(self):
        """
        Simula o lançamento do dado.

        Retorna:
        int: Valor aleatório entre 1 e 12.
        """
        return random.randint(1, self.lados)

class D20(Dado):
    """
    Representa um dado de 20 lados (D20).

    Herda de Dado e implementa o método `jogar` para retornar um valor aleatório entre 1 e 20.
    """
    def __init__(self):
        """
        Inicializa o dado com 20 lados.
        """
        super().__init__(20)

    def jogar(self):
        """
        Simula o lançamento do dado.

        Retorna:
        int: Valor aleatório entre 1 e 20.
        """
        return random.randint(1, self.lados)

