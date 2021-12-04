from unittest import TestCase
from tic_tac_toe.state import State
import tic_tac_toe.game as tic_tac_toe


class TestGame(TestCase):

    def test_actions(self):
        state = State()
        moves = tic_tac_toe.actions(state)
        #TODO reverse all of these arguments
        self.assertTrue(0x0100 in moves, "Test if this move exists in our reported moves")
        next_state = tic_tac_toe.result(state, 0x0100)
        # should have an advantage over player 2 here
        moves = tic_tac_toe.actions(next_state)
        self.assertTrue(0x0100 not in moves, "Take that action and then ensure it is not in our moves")
        self.assertEqual(next_state.player1_state, 0x0100, "Make sure our move is registered under player 1")
        self.assertEqual(tic_tac_toe.evaluating_state_function(state.player1)(next_state), 3)
        next_state = tic_tac_toe.result(next_state, 0x0010)
        moves = tic_tac_toe.actions(next_state)
        self.assertTrue(0x0010 and 0x0100 not in moves, "Remove taken moves from our move list")
        self.assertEqual(next_state.player2_state, 0x0010, "Make sure our move is registered under player 2")
        self.assertEqual(tic_tac_toe.evaluating_state_function(state.player1)(next_state), -1)
        self.assertEqual(tic_tac_toe.evaluating_state_function(state.player2)(next_state), 1)

    def test_is_early_terminal(self):
        self.assertTrue(tic_tac_toe.is_terminal(State(), False, True), "Ensure that Depth limits are respected")
        self.assertTrue(tic_tac_toe.is_terminal(State(), True, False), "Ensure that time limits are respected")

    def test_is_victory_terminal(self):
        state = State()
        state.player1_state = 0x01C0
        state.player2_state = 0x0124
        self.assertTrue(tic_tac_toe.is_terminal(state, True, True),
                        "Ensure that a winning condition masks to terminal state")
        self.assertEqual(tic_tac_toe.evaluating_state_function(state.player1)(state), 100)
        self.assertEqual(tic_tac_toe.evaluating_state_function(state.player2)(state), -100)

    def test_is_non_victory_not_terminal(self):
        state = State()
        state.player1_state = 0b000110000000
        state.player2_state = 0b000001000000
        self.assertFalse(tic_tac_toe.is_terminal(state, True, True), "Ensure same player must attain winning state")
        state.player2_state = 0b000100001110
        state.player1_state = 0b000011110000
        self.assertFalse(tic_tac_toe.is_terminal(state, True, True))
        self.assertEqual(tic_tac_toe.evaluating_state_function(state.player1)(state), 0,
                         "An inevitable draw should be score 0")

    def test_is_draw(self):
        state = State()
        state.player2_state = 0b000100001110
        state.player1_state = 0b000011110001
        self.assertTrue(tic_tac_toe.is_terminal(state, True, True), "Test draw condition")
        self.assertEqual(tic_tac_toe.evaluating_state_function(state.player1)(state), 0, "A draw should be score 0")

    def test_translate(self):
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
        player, move = tic_tac_toe.translate("1D1")
        self.assertIsNone(player)
        self.assertIsNone(move)





