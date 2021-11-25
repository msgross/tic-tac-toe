from state import State
from state import victory_conditions


def eval(state: State):
    pass


def is_victory(player_state, victory_condition):
    mask = player_state & victory_condition
    if mask ^ victory_condition == 0:
        return True

def is_terminal(state: State, is_depth_remaining: bool, is_time_remaining: bool):
    if not is_depth_remaining or not is_time_remaining:
        return True
    for victory_condition in state.victory_conditions:
        if is_victory(state.player1_state, victory_condition):
            return True
        elif is_victory(state.player2_state, victory_condition):
            return True
    return False


def result(state: State, action):
    next_state = state.copy()
    if next_state.current_player == next_state.player1:
        next_state.player1_state = next_state.player1_state | action
    else:
        next_state.player2_state = next_state.player2_state | action
    next_state.current_player = next_state.next_player()
    return next_state


def actions(state: State):

    valid_moves = []
    all_state = state.player1_state | state.player2_state
    for shift in range(0,9):
        move = 0x01 << shift
        masked_state = all_state & move
        if masked_state == 0:
            valid_moves.append(move)
    return valid_moves
