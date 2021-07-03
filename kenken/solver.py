import math
import operator
from functools import reduce
from typing import List, Tuple, Set, Dict, NamedTuple

Point = Tuple[int, int]
Board = List[List[int]]


class Rule(NamedTuple):
    op: str
    value: int
    points: Set[Point]


operators = {
    "+": sum,
    "-": lambda values: abs(reduce(operator.sub, values)),
    "/": lambda values: reduce(operator.truediv, sorted(values, reverse=True)),
    "*": math.prod,
    "=": lambda values: values[0],
}


def _find_next_empty(board: Board, board_size: int) -> Point:
    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] == -1:
                return y, x
    return -1, -1


def _validate_rule(
    board: Board, guess: int, rule: Rule, guess_y: int, guess_x: int
) -> bool:
    points = rule.points ^ {(guess_y, guess_x)}
    values = [guess]
    for y, x in points:
        if board[y][x] == -1:
            return True
        values.append(board[y][x])

    result = operators[rule.op](values)
    return result == rule.value


def _is_valid(
    board: Board, board_size: int, guess: int, rule: Rule, guess_y: int, guess_x: int
) -> bool:
    if guess in board[guess_y]:
        return False

    for i in range(board_size):
        if board[i][guess_x] == guess:
            return False

    if not _validate_rule(board, guess, rule, guess_y, guess_x):
        return False

    return True


# noinspection SpellCheckingInspection
def _solve_kenken(
    board: Board, board_size: int, rules: List[Rule], rules_lookup: Dict[Point, Rule]
) -> bool:
    guess_y, guess_x = _find_next_empty(board, board_size)
    if guess_y == -1:
        return True

    for guess in range(1, board_size + 1):
        rule = rules_lookup[(guess_y, guess_x)]
        if _is_valid(board, board_size, guess, rule, guess_y, guess_x):
            board[guess_y][guess_x] = guess

            if _solve_kenken(board, board_size, rules, rules_lookup):
                return True
        board[guess_y][guess_x] = -1
    return False


def create_empty_board(board_size: int) -> Board:
    return [[-1 for _ in range(board_size)] for _ in range(board_size)]


def solve_puzzle(board_size: int, rules: List[Rule]) -> Board:
    rules_lookup = {point: rule for rule in rules for point in rule.points}
    board = create_empty_board(board_size)
    if not _solve_kenken(board, board_size, rules, rules_lookup):
        raise ValueError("Puzzle is unsolvable")
    return board
