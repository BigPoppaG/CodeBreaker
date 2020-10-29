import random


class Board:
    """

    """

    def __init__(self, code_length, num_colours, max_turns, code=None):
        self.num_colours = num_colours
        self.code_length = code_length
        self.max_turns = max_turns
        if code is None:
            self.code = self.create_new_code()
        else:
            self.code = code

    def play(self, player='Human'):
        history = []
        while len(history) < self.max_turns:
            guess = self.get_next_guess(player)
            response = self.response(guess)
            history.append({'guess': guess, 'response': response})
            if guess == self.code:
                print('You win, Dood!')
            else:
                for turn in history:
                    print(turn)
        return history

    def get_next_guess(self, player):
        if player == 'Human':
            raw_guess = input("Guess the code. Select " + str(self.code_length) + " integers between 1 and "
                          + str(self.num_colours) + " separated with commas \n")
            self.check_guess_format(raw_guess)
            guess = self.guess_to_tuple(raw_guess)
        else:
            guess = self.generate_guess()
        return guess

    def generate_guess(self):
        return tuple(1, 1, 1, 1)

    def response(self, guess):
        """
        Black tokens given when colour and position match, white tokens given when only colour matches
        """
        blacks = [i for i in range(self.code_length) if self.code[i] == guess[i]]
        num_blacks = len(blacks)
        print('You got ' + str(num_blacks) + ' blacks')
        non_blacks = [i for i in range(self.code_length) if i not in blacks]
        remaining_code = [self.code[i] for i in non_blacks]
        whites = []
        for i in non_blacks:
            for j in range(len(remaining_code)):
                if guess[i] == remaining_code[j]:
                    whites.append(i)
                    remaining_code.pop(j)
                    break
        num_whites = len(whites)
        print('You got ' + str(num_whites) + ' whites')
        return num_blacks, num_whites

    def create_new_code(self):
        return tuple(random.randint(1, self.num_colours) for i in range(self.code_length))

    def guess_to_tuple(self, guess):
        return tuple(map(int, guess.split(',')))

    def check_guess_format(self, raw_guess):
        return True


if __name__ == '__main__':
    print("Running")
    board = Board(4, 5)
    game = board.play()
    for turn in game:
        print(turn)
