from state import State
from state import victory_conditions as victory


def is_victory(player_state, victory_condition):
    mask = player_state & victory_condition
    if mask ^ victory_condition == 0:
        return True


def evaluate_state(state: State):
    # invert the player 2 state and combine it to get available or
    p1_victory_states_possible = state.player1_state | ~state.player2_state
    p2_victory_states_possible = state.player2_state | ~state.player1_state
    # If I recall correctly, the scoring here is what bothers me.
    state_score = 0
    for victory_condition in victory:
        if is_victory(state.player1_state, victory_condition):
            state_score += 10
        if is_victory(state.player2_state, victory_condition):
            state_score += -10
        if is_victory(p1_victory_states_possible, victory_condition):
            state_score += 1
        if is_victory(p2_victory_states_possible, victory_condition):
            state_score += -1
    return state_score


def is_terminal(state: State, is_depth_remaining: bool, is_time_remaining: bool):
    if not is_depth_remaining or not is_time_remaining:
        return True
    for victory_condition in victory:
        if is_victory(state.player1_state, victory_condition):
            return True
        elif is_victory(state.player2_state, victory_condition):
            return True
    if state.player1_state | state.player2_state == 0x01FF:
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
