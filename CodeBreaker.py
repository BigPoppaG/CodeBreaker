import random


class Board:
    """

    """

    def __init__(self, code_length, num_colours, code=None):
        self.num_colours = num_colours
        self.code_length = code_length
        if code is None:
            self.code = self.create_new_code()
        else:
            self.code = code

    def play(self):
        correct = False
        while not correct:
            raw_guess = input("Guess the code. Select " + str(self.code_length) + " integers between 1 and "
                              + str(self.num_colours) + " separated with commas \n")
            self.check_guess_format(raw_guess)
            print(self.code)
            guess = self.guess_to_tuple(raw_guess)
            self.response(guess)
            correct = guess == self.code
            if correct:
                print('You win, Dood!')

    def response(self, guess):
        blacks = [i for i in range(self.code_length) if self.code[i] == guess[i]]
        print('You got ' + str(len(blacks)) + ' blacks')
        whites = []
        return blacks

    def create_new_code(self):
        return tuple(random.randint(1, self.num_colours) for i in range(self.code_length))

    def guess_to_tuple(self, guess):
        return tuple(map(int, guess.split(',')))

    def check_guess_format(self, raw_guess):
        return False


if __name__ == '__main__':
    print("Running")
    board = Board(4, 6)
    board.play()
    assert board.code_length == 4
