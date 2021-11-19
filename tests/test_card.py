import unittest
import model.card as c


class CardTest(unittest.TestCase):
    def test_eight_of_clubs(self):
        self.assertEqual(str(c.Card(8, 0)), "8 of Clubs")

    def test_eight_of_spades(self):
        self.assertEqual(str(c.Card(8, 3)), "8 of Spades")

    def test_an_eight_of_clubs_being_equal_to_an_eight_of_spades(self):
        self.assertEqual(c.Card(8, 3) > c.Card(8, 0), True)

    def test_a_queen_of_hearts_being_stronger_than_a_ten_of_diamonds(self):
        self.assertEqual(c.Card(12, 2) > c.Card(10, 1), True)


if __name__ == "__main__":
    unittest.main()
