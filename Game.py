from CodeBreaker import CodeBreaker
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
        self.code_breaker = CodeBreaker(code_length, num_colours, max_turns)

    def play(self, player='Human'):
        correct = False
        history = []
        while len(history) < self.max_turns:
            guess = self.get_next_guess(player, history)
            response = self.response(guess)
            history.append({'guess': guess, 'response': response})
            correct = guess == self.code
            if not correct:
                for turn in history:
                    print(turn)
        return self.code, history, correct

    def get_next_guess(self, player, history):
        if player == 'Human':
            legit_input = False
            while not legit_input:
                raw_guess = input("Guess the code. You have " + str(self.max_turns - len(history)) + " turns remaining."
                                    "\nSelect " + str(self.code_length) + " integers between 1 and "
                                        + str(self.num_colours) + " separated with commas."
                                    "\nOr enter 0 to let the computer take a turn.\n")
                if raw_guess == "0":
                    guess = self.code_breaker.generate_guess(history)
                    print('Using computer guess: ' + str(guess))
                    legit_input = True
                else:
                    legit_input = self.check_guess_format(raw_guess)
                    if legit_input:
                        guess = self.guess_to_tuple(raw_guess)
        else:
            guess = self.code_breaker.generate_guess(history)
        return guess

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
        try:
            self.guess_to_tuple(raw_guess)
        except ValueError:
            print('Invalid entry - try again')
            return False
        if len(self.guess_to_tuple(raw_guess)) != self.code_length:
            print('Incorrect length of guess - try again')
            return False

        return True


if __name__ == '__main__':
    board = Board(4, 5, 10)
    code, game, win = board.play()
    if win:
        print('\nYou win in ' + str(len(game)) + " moves.")
    else:
        print('\nOut of time. The correct code was: ' + str(code))
    print('This is how the game was played:')
    for turn in game:
        print(turn)
