from abc import ABC, abstractmethod
import random
from functools import total_ordering

@total_ordering  # Gera os outros métodos de comparação a partir de __eq__ e __lt__
class Dado(ABC):
    def __init__(self, lados):
        self.lados = lados

    @abstractmethod
    def jogar(self):
        pass

    def __str__(self):
        return f"Dado de {self.lados} lados"

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __eq__(self, other):
        if isinstance(other, Dado):
            return self.lados == other.lados
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Dado):
            return self.lados < other.lados
        return NotImplemented

# Subclasses específicas
class D4(Dado):
    def __init__(self):
        super().__init__(4)

    def jogar(self):
        return random.randint(1, self.lados)

class D6(Dado):
    def __init__(self):
        super().__init__(6)

    def jogar(self):
        return random.randint(1, self.lados)

class D8(Dado):
    def __init__(self):
        super().__init__(8)

    def jogar(self):
        return random.randint(1, self.lados)

class D10(Dado):
    def __init__(self):
        super().__init__(10)

    def jogar(self):
        return random.randint(1, self.lados)

class D12(Dado):
    def __init__(self):
        super().__init__(12)

    def jogar(self):
        return random.randint(1, self.lados)

class D20(Dado):
    def __init__(self):
        super().__init__(20)

    def jogar(self):
        return random.randint(1, self.lados)

