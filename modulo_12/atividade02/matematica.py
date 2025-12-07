# Arquivo: matematica.py

class Calculadora:
    """
    Uma classe simples para realizar operações matemáticas básicas.
    """
    def somar(self, a, b):
        """Retorna a soma de a e b."""
        return a + b

    def subtrair(self, a, b):
        """Retorna a diferença entre a e b."""
        return a - b

    def multiplicar(self, a, b):
        """Retorna o produto de a e b."""
        return a * b

    def dividir(self, a, b):
        """Retorna a divisão de a por b."""
        if b == 0:
            # Esta linha será importante para o Exercício 3!
            raise ValueError("Não é possível dividir por zero.")
        return a / b