"""
Unit tests for tic-tac-toe game rules
"""

from unittest import TestCase
from tic_tac_toe.state import State
import tic_tac_toe.game as tic_tac_toe


class TestGame(TestCase):
    """
    Test game class, unit tests
    """
    def test_actions(self):
        """
        Test actions and resulting states
        """
        state = State()
        moves = tic_tac_toe.actions(state)
        self.assertTrue(0x0100 in moves, "Test if this move exists in our reported moves")
        next_state = tic_tac_toe.result(state, 0x0100)
        # should have an advantage over player 2 here
        moves = tic_tac_toe.actions(next_state)
        self.assertTrue(0x0100 not in moves, "Take that action and then ensure it is not in our moves")
        self.assertEqual(0x0100, next_state.player1_state, "Make sure our move is registered under player 1")
        self.assertEqual(3, tic_tac_toe.evaluating_state_function(state.player1)(next_state),
                         "Should be 8 potential victory states minus 5 losing states")
        next_state = tic_tac_toe.result(next_state, 0x0010)
        moves = tic_tac_toe.actions(next_state)
        self.assertTrue(0x0010 and 0x0100 not in moves, "Remove taken moves from our move list")
        self.assertEqual(0x0010, next_state.player2_state, "Make sure our move is registered under player 2")
        self.assertEqual(-1, tic_tac_toe.evaluating_state_function(state.player1)(next_state),
                         "After player 2 moves, player 1 is now at a disadvantage")
        self.assertEqual(1, tic_tac_toe.evaluating_state_function(state.player2)(next_state),
                         "After player 2 moves, player 2 is at a slight advantage")

    def test_is_early_terminal(self):
        """
        Method tests that early termination conditions actually result in early termination
        """
        self.assertTrue(tic_tac_toe.is_terminal(State(), False, True), "Ensure that Depth limits are respected")
        self.assertTrue(tic_tac_toe.is_terminal(State(), True, False), "Ensure that time limits are respected")

    def test_is_victory_terminal(self):
        """
        Test that victory conditions results in termination returning True
        """
        state = State()
        state.player1_state = 0x01C0
        state.player2_state = 0x0124
        self.assertTrue(tic_tac_toe.is_terminal(state, True, True),
                        "Ensure that a winning condition masks to terminal state")
        self.assertEqual(100, tic_tac_toe.evaluating_state_function(state.player1)(state), "Winning is +100")
        self.assertEqual(-100, tic_tac_toe.evaluating_state_function(state.player2)(state), "Losing is -100")

    def test_is_non_victory_not_terminal(self):
        """
        Method tests that not winning does not result in a terminal condition
        """
        state = State()
        state.player1_state = 0b000110000000
        state.player2_state = 0b000001000000
        self.assertFalse(tic_tac_toe.is_terminal(state, True, True),
                         "Make sure that three-in-a-row condition must be fulfilled by a single player")
        state.player2_state = 0b000100001110
        state.player1_state = 0b000011110000
        self.assertFalse(tic_tac_toe.is_terminal(state, True, True))
        self.assertEqual(0,tic_tac_toe.evaluating_state_function(state.player1)(state),
                         "An inevitable draw should be score 0")

    def test_is_draw(self):
        """
        Unit test for draw condition  resulting in terminating state
        """
        state = State()
        state.player2_state = 0b000100001110
        state.player1_state = 0b000011110001
        self.assertTrue(tic_tac_toe.is_terminal(state, True, True), "Test draw condition")
        self.assertEqual(0, tic_tac_toe.evaluating_state_function(state.player1)(state), "A draw should be score 0")

    def test_translate(self):
        """
        Unit test for translation method
        Should exercise both valid and invalid requested actions to take
        """
        player, move = tic_tac_toe.translate("1C1")
        self.assertEqual(1, player, "Translate the player as player 1")
        self.assertEqual(0x0001, move, "Move should go in  the bottom right corner")
        player, move = tic_tac_toe.translate("2B2")
        self.assertEqual(2, player, "Translate the player as player 1")
        self.assertEqual(0x0010, move, "Move should go in the center")
        player, move = tic_tac_toe.translate("1A3")
        self.assertEqual(1, player, "Translate the player as player 1")
        self.assertEqual(0x0100, move, "Move should go in top left corner")

    def test_invalid_translate(self):
        """
        Unit test to ensure translate returns [None, None] if a
        move is invalid
        """
        player, move = tic_tac_toe.translate("1D1")
        self.assertIsNone(player)
        self.assertIsNone(move)





