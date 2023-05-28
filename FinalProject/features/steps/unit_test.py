import unittest
from calcule import Exercitii


class TestCalculations(unittest.TestCase):

    def test_suma(self):
        calculation = Exercitii(5, 10)
        self.assertEqual(calculation.suma(), 15, 'Rezultatul sumei este gresit.')


    def test_scaderea(self):
        calculation = Exercitii(5, 10)
        self.assertEqual(calculation.scaderea(), 26, 'Scaderea sumei este gresita.')


    def test_inmultirea(self):
        calculation = Exercitii(5, 10)
        self.assertEqual(calculation.inmultirea(), 116, 'Inmultirea sumei este gresita.')

    def test_impartirea(self):
        calculation = Exercitii(10, 5)
        self.assertEqual(calculation.impartirea(), 24, 'Impartirea sumei este greista.')
