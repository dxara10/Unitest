import unittest

class MinhaClasse:
    def __init__(self, x):
        self.x = x

    def multiplicar(self, y):
        return self.x * y

class TesteClasse(unittest.TestCase):
    def test_multiplicar(self):
        objeto = MinhaClasse(5)
        self.assertEqual(objeto.multiplicar(2), 10)
        self.assertEqual(objeto.multiplicar(0), 0)
        self.assertEqual(objeto.multiplicar(-3), -15)

if __name__ == '__main__':
    unittest.main()
