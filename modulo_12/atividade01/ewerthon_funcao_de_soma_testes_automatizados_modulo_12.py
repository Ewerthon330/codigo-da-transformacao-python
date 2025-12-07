# Arquivo: test_matematica.py

import unittest
from matematica import soma  # Importa a função que você quer testar

class TestSoma(unittest.TestCase):
    """
    Classe de testes para a função 'soma' do módulo matematica.
    """

    def test_soma_numeros_positivos(self):
        """
        Testa se a função soma funciona corretamente com dois números positivos.
        """
        # O método assertEqual verifica se o primeiro argumento é igual ao segundo.
        resultado = soma(5, 7)
        self.assertEqual(resultado, 12, "Deve ser 12 para 5 + 7")

    def test_soma_com_zero(self):
        """
        Testa a soma de um número positivo com zero.
        """
        resultado = soma(10, 0)
        self.assertEqual(resultado, 10, "Deve ser 10 para 10 + 0")

    def test_soma_numeros_negativos(self):
        """
        Testa a soma de dois números negativos.
        """
        resultado = soma(-5, -3)
        self.assertEqual(resultado, -8, "Deve ser -8 para -5 + -3")

    def test_soma_numero_positivo_e_negativo(self):
        """
        Testa a soma de um número positivo com um negativo.
        """
        resultado = soma(10, -3)
        self.assertEqual(resultado, 7, "Deve ser 7 para 10 + -3")

# Isso garante que os testes sejam executados quando o arquivo é rodado diretamente
if __name__ == '__main__':
    unittest.main()