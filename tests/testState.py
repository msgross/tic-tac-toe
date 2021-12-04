"""
Unit tests for the State class
"""

from unittest import TestCase
from tic_tac_toe.state import State


class TestState(TestCase):
    """
    Test State class
    """
    def test_copy(self):
        """
        Method tests that the copy method provides an accurate copy of the state
        """
        original_state = State()
        original_state.player1_state = 0x01
        original_state.player2_state = 0x10
        self.assertEqual(original_state, original_state.copy(), "Ensure states are equal between copies")

    def test_next_turn(self):
        """
        Test that the next_player method returns the right player
        """
        original_state = State()
        self.assertEqual(original_state.next_player(), original_state.player2)
        next_state = original_state.copy()
        next_state.current_player = next_state.next_player()
        self.assertEqual(next_state.next_player(), original_state.player1)
