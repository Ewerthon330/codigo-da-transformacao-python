import unittest
from calculadora import Calculadora # Importe sua classe Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        """Prepara uma nova instância da calculadora para cada teste."""
        self.calc = Calculadora()

    # ... (Seus testes dos exercícios 1 e 2 viriam aqui, como somar) ...

    # TESTE PARA DIVISÃO POR ZERO (EXERCÍCIO 3)
    def test_divisao_por_zero(self):
        """
        Verifica se a divisão por zero levanta corretamente a exceção ZeroDivisionError.
        """
        # self.assertRaises(Tipo_de_Excecao, Funcao_a_Testar, *Argumentos)
        
        # Cenário: Tentar dividir 10 por 0
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)
            
        # Você também pode verificar se a mensagem da exceção é a esperada:
        with self.assertRaisesRegex(ZeroDivisionError, "Divisão por zero não é permitida"):
            self.calc.dividir(5, 0)

    # TESTE PARA OUTRAS ENTRADAS INVÁLIDAS (Opcional, dependendo da sua implementação)
    def test_divisao_com_entrada_nao_numerica(self):
        """
        Verifica se entradas inválidas (não números) levantam o TypeError.
        Isto depende de como o Python trata a operação subjacente.
        """
        # Se sua função dividir não lida com strings, Python levantará TypeError
        with self.assertRaises(TypeError):
            self.calc.dividir(10, "a")

if __name__ == '__main__':
    unittest.main()