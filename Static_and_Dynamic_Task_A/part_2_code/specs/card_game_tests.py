import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.game = CardGame()
        self.card_1 = Card("Clubs", 10)
        self.card_2 = Card("Hearts", 4)
        self.card_3 = Card("Spades",1)
        self.cards = [self.card_1, self.card_2, self.card_3]
    
    def test_check_for_ace_true(self):
        game1 = self.game.check_for_ace(self.card_3)
        self.assertEqual(True, game1)

    def test_check_for_ace_false(self):
        game2 = self.game.check_for_ace(self.card_2)
        self.assertEqual(False, game2)

    def test_highest_card_card1_highest(self):
        game3 = self.game.highest_card(self.card_1, self.card_2,)
        self.assertEqual(self.card_1, game3)

    def test_highest_card_card2_highest(self):
        game4 = self.game.highest_card(self.card_2, self.card_1)
        self.assertEqual(self.card_1, game4)

    def test_cards_total(self):
        game5 = self.game.cards_total(self.cards)
        self.assertEqual("You have a total of 15", game5)