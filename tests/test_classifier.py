import unittest
from app.classifier import classificar_produto 

class TestBalanca(unittest.TestCase):

    def test_produto_leve(self):
        # Testando peso abaixo de 0.5
        resultado = classificar_produto(0.2)
        self.assertEqual(resultado, "Produto leve 🪶")

    def test_produto_medio(self):
        # Testando peso entre 0.5 e 2
        resultado = classificar_produto(1.5)
        self.assertEqual(resultado, "Produto médio 📦")

    def test_produto_pesado(self):
        # Testando peso acima de 2
        resultado = classificar_produto(3.0)
        self.assertEqual(resultado, "Produto pesado 🏋️")

if __name__ == '__main__':
    unittest.main()