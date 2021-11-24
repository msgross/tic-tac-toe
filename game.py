import numpy as np
import numpy.ma as mask
from state import State
from state import victory_conditions


def eval(state: State):
    pass


def is_terminal(state: State, is_depth_remaining: bool, is_time_remaining: bool):
    if not is_depth_remaining or not is_time_remaining:
        return True
    for victory_condition in victory_conditions:
        mask_out_p1 = mask.masked_equal(state.state, state.player1)
        mask_out_p2 = mask.masked_equal(state.state, state.player2)
        mask.filled(mask_out_p1, fill_value = )


def result(state: State, action):
    next_state = state.copy()
    next_state.state[action[0], action[1]] = next_state.current_player
    next_state.current_player = next_state.next_player()
    return next_state


def actions(state: State):
    return np.asarray(state.state == 0).nonzero()
