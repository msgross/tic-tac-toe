from enum import Enum

# Possible victory states


_horiz_top = 0x01C0   # 000111000000
_horiz_center = 0x38  # 000000111000
_horiz_bottom = 0x07  # 000000000111

_vert_left = 0x0124   # 000100100100
_vert_center = 0x92   # 000010010010
_vert_right = 0x49     # 000001001001

_diag_right = 0x0111  # 000100010001
_diag_left = 0x54    # 000001010100


victory_conditions = [_horiz_top, _horiz_center, _horiz_bottom,
                      _vert_left, _vert_center, _vert_right,
                      _diag_right, _diag_left]


class State:
    def __eq__(self, other):
        return self.current_player == other.current_player and \
            self.player1_state == other.player1_state and \
            self.player2_state == other.player2_state

    def __init__(self):
        self.player1 = 1
        self.player2 = 2
        self.current_player = self.player1
        self.player1_state = 0x0000
        self.player2_state = 0x0000

    def copy(self):
        copy_state = State()
        copy_state.current_player = self.current_player
        copy_state.player1_state = self.player1_state
        copy_state.player2_state = self.player2_state
        return copy_state

    def next_player(self):
        return self.player1 if self.current_player == self.player2 else self.player2
