import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

# The FrenchDeck class from the Fluent Python text
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split(" ")

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return "A standard deck of cards."

# Convert the user input to a list and title case
names = input('Enter a list of space separated names: ').title().split(" ")

# Remove any extra spaces a user may have entered
names = [name for name in names if name != '']

# Multiply the names list to have >= 52 items
length = -(-52 // len(names))
names *= length

# This number will determine the final turn
num = random.randint(20,52)

# Instantiate the deck
deck = FrenchDeck()
random.shuffle(deck._cards)

def flag():
    """A function to determine if the user would like to continue."""

    response = input('Continue? Y/N: ')

    if response.lower().strip() == 'n':
        print("You've ended the game.")
        return False

    else:
        return True

count, turn = 0, 1

while flag():
    if count >= num:
        print(f'Game over, {names[count]} has lost.')
        break

    current_name = names[count]
    current_card = deck._cards[count]
    print(f'Turn: {turn}')
    print(f'{current_name} drew {current_card}')
    count += 1
    turn += 1
