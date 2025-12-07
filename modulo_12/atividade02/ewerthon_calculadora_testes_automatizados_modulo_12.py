# Arquivo: test_calculadora.py

import unittest
from matematica import Calculadora # Importa a classe

class TestCalculadora(unittest.TestCase):
    """
    Classe de testes para a Calculadora, com métodos para somar e dividir.
    """

    # --- Método de Setup ---
    # Este método é executado ANTES de cada método de teste.
    def setUp(self):
        """Inicializa uma nova instância da Calculadora para cada teste."""
        self.calc = Calculadora() 
        print(f"Executando setup para o teste: {self._testMethodName}")
        # self.calc agora está disponível em todos os métodos de teste

    # --- Testes de Somar ---
    def test_somar_numeros_positivos(self):
        """Verifica 5 + 7 = 12."""
        resultado = self.calc.somar(5, 7)
        self.assertEqual(resultado, 12)

    def test_somar_numeros_negativos(self):
        """Verifica -10 + -5 = -15."""
        resultado = self.calc.somar(-10, -5)
        self.assertEqual(resultado, -15)
    
    # --- Testes de Multiplicar ---
    def test_multiplicar_simples(self):
        """Verifica 3 * 4 = 12."""
        resultado = self.calc.multiplicar(3, 4)
        self.assertEqual(resultado, 12)

    # --- Testes de Dividir ---
    def test_dividir_numeros_inteiros(self):
        """Verifica 10 / 2 = 5."""
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5)

    def test_dividir_com_ponto_flutuante(self):
        """Verifica 10 / 4 = 2.5."""
        resultado = self.calc.dividir(10, 4)
        self.assertEqual(resultado, 2.5)


# Executa todos os testes se o arquivo for rodado diretamente
if __name__ == '__main__':
    unittest.main()