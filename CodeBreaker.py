def test():
    board = Board((1, 2, 1, 3), 5)

    assert board.code_length == 4


class Board:
    """

    """

    def __init__(self, code, num_colours):
        self.code = code
        self.num_colours = num_colours
        self.code_length = len(self.code)

