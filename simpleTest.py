import unittest

class TesteIgualdade(unittest.TestCase):
    def test_igualdade(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()
