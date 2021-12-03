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


class Status(Enum):
    IN_PROGRESS = 0
    DONE = 1
    ILLEGAL_STATE = -1


class State:
    def __init__(self):
        self.empty = 0
        self.player1 = 1
        self.player2 = 2
        self.current_player = self.player1
        self.player1_state = 0x0000
        self.player2_state = 0x0000
        self.status = Status.IN_PROGRESS
        self.winner = None

    def copy(self):
        copy_state = State()
        copy_state.current_player = self.current_player
        copy_state.status = self.status
        copy_state.player1_state = self.player1_state.copy()
        copy_state.player2_state = self.player2_state.copy()
        return copy_state

    def next_player(self):
        return 1 if self.current_player is 0 else 0
