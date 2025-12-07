class Calculadora:
    """
    Uma classe simples para demonstrar operações matemáticas.
    """
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            # Esta linha garante que o erro correto seja lançado
            raise ZeroDivisionError("Divisão por zero não é permitida")
        return a / b