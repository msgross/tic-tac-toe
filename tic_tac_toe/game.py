"""
Defines game rules for tic-tac-toe
"""

from tic_tac_toe.state import State
from tic_tac_toe.state import victory_conditions as victory

# mask out the bits we aren't using for evaluation
__MASK = 0x01ff  # 0000000111111111


def __is_victory(player_state, victory_condition):
    """
    Returns true if the provided state represents a provided victory state
    :param player_state: The state under evaluation
    :param victory_condition: The victory condition to test against
    :return: True if the state represents the provided victory condition, false otherwise
    """
    mask = player_state & victory_condition
    if mask ^ victory_condition == 0:
        return True


def __score(current_player_state, opposing_player_state):
    """
    Method returns a score for a given player which
    either returns an overwhelming score in victory or loss or the delta
    between available current player victory conditions and opposing player
    victory conditions. A positive value means that the current player
    has more victory opportunities, a negative value means that the opposing
    player has more victory opportunities
    :param current_player_state: the current player state
    :param opposing_player_state: the opposing player state
    :return: the evaluated score for the given state
    """
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
    """
    Method returns the score of a given maximizing player.
    :param maximizing_player: the player whose score we're currently maximizing
    :param state: the state to score
    :return: the evaluated score
    """
    if maximizing_player == state.player1:
        return __score(state.player1_state, state.player2_state)
    else:
        return __score(state.player2_state, state.player1_state)


def evaluating_state_function(maximizing_player):
    """
    Method returns a function that scores a state,
    based on the player who is being scored
    :param maximizing_player:  the player being scored
    :return: a function that scores a given tic-tac-toe state
    """
    return lambda s: __evaluating_state_function(maximizing_player, s)


def is_terminal(state: State, is_depth_remaining: bool, is_time_remaining: bool):
    """
    Method returns whether a state represents a terminal state for the game
    :param state: the state under evaluation
    :param is_depth_remaining: True if a tree-search function can continue in depth, False otherwise
    :param is_time_remaining: True if time remains for a search function to operate, False otherwise
    :return: True if the state represents a terminal state (no moves remaining, someone won, or a tie),
             False otherwise
    """
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
    """
    Method returns the state that results from a given action
    :param state: the state under evaluation
    :param action: the action to take
    :return: the state that results from the given state
    """
    next_state = state.copy()
    if next_state.current_player == next_state.player1:
        next_state.player1_state = next_state.player1_state | action
    else:
        next_state.player2_state = next_state.player2_state | action
    next_state.current_player = next_state.next_player()
    return next_state


def actions(state: State):
    """
    Method returns a list of possible moves given the current state.
    Just searches for missing bits in our state
    :param state: the state under evaluation
    :return: list of possible moves
    """
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

