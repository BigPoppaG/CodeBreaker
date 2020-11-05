from Game import Board
import random


def GenerateTests(NumTrials, code_length=0, num_colours=0, max_turns=0):

    for trial in range(NumTrials):
        if code_length == 0: code_length = random.randint(3, 6)
        if num_colours == 0: num_colours = random.randint(3, 7)
        if max_turns == 0: max_turns = 20

        board = Board(code_length, num_colours, max_turns)
        code = board.code

        yield code_length, num_colours, max_turns, code

