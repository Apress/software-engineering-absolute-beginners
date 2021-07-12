class WinningSequence:

    winning_sequence = (1, 3, 12, 14, 15)

    def validate(self, number) -> bool:
        for in_sequence in self.winning_sequence:
            if in_sequence == number:
                return True
        return False

'''
The new Lotto class does not concern itself with how Lotto numbers
are checked. It uses the Sequence class to do so
'''
class Lotto:

    def __init__(self):
        self.sequence = WinningSequence()

    def is_winner(self, number: int) -> bool:
        return self.sequence.validate(number)

lotto = Lotto()
# Initialise the message variable
lotto_message = 'You do not have a winning number'
if lotto.is_winner(3):
	lotto_message = 'You have a winning number'
print(lotto_message)
