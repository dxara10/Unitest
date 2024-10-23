import unittest

def dobrar(numero):
    return numero * 2

class TesteComportamento(unittest.TestCase):
    def test_dobrar(self):
        self.assertEqual(dobrar(5), 10)
        self.assertEqual(dobrar(0), 0)
        self.assertEqual(dobrar(-3), -6)

if __name__ == '__main__':
    unittest.main()
