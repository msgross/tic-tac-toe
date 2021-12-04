"""
Defines the state for tic-tac-toe

Since the possible state tree is fairly small,
we encode potential moves as a bit encoding
"""

# Possible victory states
# a top row victory state
_horiz_top = 0x01C0   # 0000000111000000
# a center row victory state
_horiz_center = 0x38  # 0000000000111000
# a bottom row victory state
_horiz_bottom = 0x07  # 0000000000000111
# a left column victory state
_vert_left = 0x0124   # 0000000100100100
# a center column victory state
_vert_center = 0x92   # 0000000010010010
# a right column victory state
_vert_right = 0x49    # 0000000001001001
# a diagonal down to the right victory state
_diag_right = 0x0111  # 0000000100010001
# a diagonal up to the left victory state
_diag_left = 0x54     # 0000000001010100

# create a list of these victory conditions for reference
victory_conditions = [_horiz_top, _horiz_center, _horiz_bottom,
                      _vert_left, _vert_center, _vert_right,
                      _diag_right, _diag_left]


class State:
    """
    Represents a tic-tac-toe game state
    """
    def __eq__(self, other):
        """ Overrides __eq__ """
        return self.current_player == other.current_player and \
            self.player1_state == other.player1_state and \
            self.player2_state == other.player2_state

    def __init__(self):
        """
        Constructor--initializes the game
        """
        self.player1 = 1
        self.player2 = 2
        self.current_player = self.player1
        self.player1_state = 0x0000
        self.player2_state = 0x0000

    def copy(self):
        """
        Copy method
        :return: a copy of this state
        """
        copy_state = State()
        copy_state.current_player = self.current_player
        copy_state.player1_state = self.player1_state
        copy_state.player2_state = self.player2_state
        return copy_state

    def next_player(self):
        """
        :return: The next player to go
        """
        return self.player1 if self.current_player == self.player2 else self.player2
