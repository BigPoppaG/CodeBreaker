import itertools
import time


def test():
    board = Board((1, 2, 1, 3), 5)

    assert powerset([1, 2, 3]) == {(1,), (2,), (3,), (1, 2), (1, 3), (2, 3)}
    assert board.get_neighbours((1, 1)) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}






class Board:
    """

    """

    def __init__(self, code, num_colours):
        self.code = code
        self.num_colours = num_colours

