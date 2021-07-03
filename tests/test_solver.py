from typing import List

import pytest

from kenken.solver import solve_puzzle, Rule, Board

test_6_size_board = [
    6,
    [
        Rule("-", 1, {(0, 0), (1, 0)}),
        Rule("+", 11, {(0, 1), (1, 1), (1, 2)}),
        Rule("-", 4, {(0, 2), (0, 3)}),
        Rule("*", 60, {(0, 4), (0, 5), (1, 4)}),
        Rule("=", 4, {(1, 3)}),
        Rule("-", 4, {(1, 5), (2, 5)}),
        Rule("+", 7, {(2, 0), (2, 1), (2, 2)}),
        Rule("/", 2, {(2, 3), (2, 4)}),
        Rule("-", 3, {(3, 0), (3, 1)}),
        Rule("+", 7, {(3, 2), (3, 3), (4, 3)}),
        Rule("-", 5, {(3, 4), (4, 4)}),
        Rule("+", 9, {(3, 5), (4, 5), (5, 5)}),
        Rule("-", 1, {(4, 0), (5, 0)}),
        Rule("-", 5, {(4, 1), (5, 1)}),
        Rule("+", 8, {(4, 2), (5, 2)}),
        Rule("-", 1, {(5, 3), (5, 4)}),
    ],
    [
        [4, 3, 1, 5, 2, 6],
        [3, 2, 6, 4, 5, 1],
        [1, 4, 2, 6, 3, 5],
        [2, 5, 4, 1, 6, 3],
        [5, 6, 3, 2, 1, 4],
        [6, 1, 5, 3, 4, 2],
    ],
]

test_5_size_board = [
    5,
    [
        Rule("+", 11, {(0, 0), (0, 1), (1, 0), (2, 0)}),
        Rule("*", 20, {(0, 2), (0, 3), (0, 4)}),
        Rule("-", 1, {(1, 1), (1, 2)}),
        Rule("+", 6, {(1, 3), (2, 3)}),
        Rule("-", 3, {(1, 4), (2, 4)}),
        Rule("-", 2, {(2, 1), (2, 2)}),
        Rule("-", 4, {(3, 0), (3, 1)}),
        Rule("/", 2, {(3, 2), (4, 2)}),
        Rule("*", 6, {(3, 3), (4, 3)}),
        Rule("-", 1, {(3, 4), (4, 4)}),
        Rule("-", 1, {(4, 0), (4, 1)}),
    ],
    [
        [3, 2, 5, 4, 1],
        [2, 3, 4, 1, 5],
        [4, 1, 3, 5, 2],
        [1, 5, 2, 3, 4],
        [5, 4, 1, 2, 3],
    ],
]

test_4_size_board = [
    4,
    [
        Rule("/", 2, {(0, 0), (1, 0)}),
        Rule("*", 6, {(0, 1), (0, 2), (0, 3)}),
        Rule("+", 8, {(1, 1), (2, 1), (2, 2), (3, 2)}),
        Rule("-", 1, {(1, 2), (1, 3)}),
        Rule("-", 2, {(2, 0), (3, 0)}),
        Rule("=", 4, {(3, 1)}),
        Rule("-", 1, {(2, 3), (3, 3)}),
    ],
    [[4, 3, 2, 1], [2, 1, 3, 4], [1, 2, 4, 3], [3, 4, 1, 2]],
]


@pytest.mark.parametrize(
    ["board_size", "rules", "solution"],
    [test_6_size_board, test_5_size_board, test_4_size_board],
)
def test_solve_puzzle(board_size: int, rules: List[Rule], solution: Board) -> None:
    # noinspection PyTypeChecker
    assert solve_puzzle(board_size, rules) == solution


def test_unsolvable_puzzle() -> None:
    with pytest.raises(ValueError):
        solve_puzzle(
            3,
            [
                Rule(
                    "+",
                    10,
                    {
                        (0, 0),
                        (0, 1),
                        (0, 2),
                        (1, 0),
                        (1, 1),
                        (1, 2),
                        (2, 0),
                        (2, 1),
                        (2, 2),
                    },
                )
            ],
        )
