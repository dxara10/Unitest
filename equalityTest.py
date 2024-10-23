import unittest

class TesteIgualdadeFlutuante(unittest.TestCase):
    def test_igualdade_flutuante(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, delta=0.0001)

if __name__ == '__main__':
    unittest.main()
