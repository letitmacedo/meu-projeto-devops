# test_app.py

import unittest
import app  # importa seu app.py

class TestApp(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(app.soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(app.subtracao(5, 3), 2)

    def test_multiplicacao(self):
        self.assertEqual(app.multiplicacao(2, 3), 6)

    def test_divisao(self):
        self.assertEqual(app.divisao(6, 3), 2)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            app.divisao(5, 0)

if __name__ == '__main__':
    unittest.main()
