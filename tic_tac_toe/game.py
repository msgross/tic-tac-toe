from tic_tac_toe.state import State
from tic_tac_toe.state import victory_conditions as victory

# mask out the bits we aren't using for evaluation
__MASK = 0x01ff


def __is_victory(player_state, victory_condition):
    mask = player_state & victory_condition
    if mask ^ victory_condition == 0:
        return True


def __score(current_player_state, opposing_player_state):
    current_player_victory_states_possible = (current_player_state | ~(opposing_player_state & __MASK)) & __MASK
    opposing_player_victory_states_possible = (opposing_player_state | ~(current_player_state& __MASK)) & __MASK

    current_player_score = 0
    opposing_player_score = 0
    for victory_condition in victory:
        if __is_victory(current_player_state, victory_condition):
            return 100
        if __is_victory(opposing_player_state, victory_condition):
            return -100
        if __is_victory(current_player_victory_states_possible, victory_condition):
            current_player_score += 1
        if __is_victory(opposing_player_victory_states_possible, victory_condition):
            opposing_player_score += 1

    return current_player_score - opposing_player_score


def __evaluating_state_function(maximizing_player, state):
    if maximizing_player == state.player1:
        return __score(state.player1_state, state.player2_state)
    else:
        return __score(state.player2_state, state.player1_state)


def evaluating_state_function(maximizing_player):
    return lambda s: __evaluating_state_function(maximizing_player, s)


def is_terminal(state: State, is_depth_remaining: bool, is_time_remaining: bool):
    if not is_depth_remaining or not is_time_remaining:
        return True
    for victory_condition in victory:
        if __is_victory(state.player1_state, victory_condition):
            return True
        elif __is_victory(state.player2_state, victory_condition):
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
    for shift in range(0, 9):
        move = 0x01 << shift
        masked_state = all_state & move
        if masked_state == 0:
            valid_moves.append(move)
    return valid_moves


def translate(command):
    """
    Translate the serialization of a move into an action that the game can consume
    :param command: Representation of a move to be taken that can be translated into an action
    :return: the translated action
    """
    command_player = command[0:1]
    if command_player != "1" and command_player != "2":
        return None, None
    player = int(command_player)

    move = 0x0001
    x_direction = command[1:2].lower()
    if x_direction == "a":
        move = move << 2
    elif x_direction == "b":
        move = move << 1
    elif x_direction == "c":
        move = move << 0
    else:
        return None, None

    y_direction = command[2:3].lower()
    y_val = int(y_direction)
    if y_val == 1:
        move = move << 0
    elif y_val == 2:
        move = move << 3
    elif y_val == 3:
        move = move << 6
    else:
        return None, None
    return player, move

