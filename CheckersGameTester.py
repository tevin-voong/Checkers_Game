# Author: Tevin Voong
# GitHub username: tevinvoong
# Date: 3/16/2023
# Description: Unit Test file for checkers

import unittest
from CheckersGame import Checkers

class TestCheckers(unittest.TestCase):

    def test_1(self):
        """Tests get checker details"""
        game = Checkers()
        Player1 = game.create_player("Adam", "White")
        game.play_game("Adam", (2, 1), (3, 2))
        self.assertEqual(game.get_checker_details((3, 2)), 'White')

    def test_2(self):
        """Tests print board method"""
        game = Checkers()
        Player2 = game.create_player("Lucy", "Black")
        game.play_game("Lucy", (5, 0), (4, 1))
        self.assertEqual(game.print_board(), [[None, 'White', None, 'White', None, 'White', None, 'White'], ['White', None, 'White', None, 'White', None, 'White', None], [None, 'White', None, 'White', None, 'White', None, 'White'], [None, None, None, None, None, None, None, None], [None, 'Black', None, None, None, None, None, None], [None, None, 'Black', None, 'Black', None, 'Black', None], [None, 'Black', None, 'Black', None, 'Black', None, 'Black'], ['Black', None, 'Black', None, 'Black', None, 'Black', None]])

    def test_3(self):
        """Tests if movement of a colored piece worked"""
        game = Checkers()
        Player1 = game.create_player("Adam", "White")
        Player2 = game.create_player("Lucy", "Black")
        game.play_game("Lucy", (5, 0), (4, 1))
        game.play_game("Adam", (2, 1), (3, 2))
        self.assertIs(game.get_checker_details((4, 1)), "Black")

    def test_4(self):
        """Tests if game has not ended"""
        game = Checkers()
        Player1 = game.create_player("Adam", "White")
        Player2 = game.create_player("Lucy", "Black")
        game.play_game("Lucy", (5, 0), (4, 1))
        game.play_game("Adam", (2, 1), (3, 2))
        self.assertEqual(game.game_winner(), "Game has not ended.")

    def test_5(self):
        """Tests that conversion to King was successful"""
        game = Checkers()
        Player1 = game.create_player("Adam", "White")
        Player2 = game.create_player("Lucy", "Black")
        game.play_game("Lucy", (5, 0), (4, 1))
        game.play_game("Adam", (2, 1), (3, 2))
        game.play_game("Lucy", (5, 2), (4, 3))
        game.play_game("Adam", (3, 2), (5, 0))
        game.play_game("Lucy", (4, 3), (3, 4))
        game.play_game("Adam", (2, 3), (4, 5))
        game.play_game("Lucy", (5, 6), (3, 4))
        game.play_game("Adam", (2, 5), (4, 3))
        game.play_game("Lucy", (5, 4), (3, 2))
        game.play_game("Adam", (2, 7), (3, 6))
        game.play_game("Lucy", (6, 1), (5, 2))
        game.play_game("Adam", (1, 0), (2, 1))
        game.play_game("Lucy", (3, 2), (1, 0))
        game.play_game("Adam", (1, 2), (2, 3))
        game.play_game("Lucy", (7, 2), (6, 1))
        game.play_game("Adam", (5, 0), (7, 2))
        self.assertIs(game.get_checker_details((7, 2)), "White_King")
