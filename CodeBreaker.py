import random


class CodeBreaker:
    def __init__(self, code_length, num_colours, max_turns):
        self.num_colours = num_colours
        self.code_length = code_length
        self.max_turns = max_turns

    def generate_guess(self, history):
        keep_guessing = True
        while keep_guessing:
            guess = tuple(random.randint(1, self.num_colours) for i in range(self.code_length))
            if not any(turn['guess'] == guess for turn in history):
                keep_guessing = False
        return guess
