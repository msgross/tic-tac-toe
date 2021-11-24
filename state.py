import numpy as np
from enum import Enum

# Possible victory states


_horiz_top = np.array([(1, 1, 1), (0, 0, 0), (0, 0, 0)])
_horiz_center = np.array([(0, 0, 0), (1, 1, 1), (0, 0, 0)])
_horiz_bottom = np.array([(0, 0, 0), (0, 0, 0), (1, 1, 1)])

_vert_left = np.array([(1, 0, 0), (1, 0, 0), (1, 0, 0)])
_vert_center = np.array([(0, 1, 0), (0, 1, 0), (0, 1, 0)])
_vert_right = np.array([(0, 0, 1), (0, 0, 1), (0, 0, 1)])

_diag_right = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
_diag_left = np.array([(0, 0, 1), (0, 1, 0), (1, 0, 0)])

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
        self.state = np.zeros([3, 3], dtype=int)
        self.status = Status.IN_PROGRESS

    def copy(self):
        copy_state = State()
        copy_state.current_player = self.current_player
        copy_state.status = self.status
        copy_state.state = self.state.copy()
        return copy_state

    def next_player(self):
        return 1 if self.current_player is 0 else 0
