"""This class is meant to be a holder for the deck object.

    Totalling 54 cards, a standard deck of cards is composed of 4 sequences from Ace to King 
in 4 suits - Spades, Hearts, Clubs and Diamonds; besides that, most deck of cards come with 
two Jokers, black and red. 

    In essence, we will represent such deck of cards as a simple sequence list of strings, where
a sequence is represented by the number and its suit, as [AS, 1S, 2S, ...]

Shuffling
---------

    Before talking about shuffling the deck, it is important to determ what an unshuffled deck is:
I consider it to be consisted by the increasing sequences with suits in order of: Spades, Hearts, 
Clubs and Diamonds; I used such definition after buying a new deck of cards and observing it came
in such order from the manufecturer. 

    Shuffling the deck will increase the entropy. Maximizing the such increase can be done by 
splitting the deck in half and stacking the top card form each half one after the other. It is
easy to picture it, just think of how those professional dealers in Cassinos shuffle cards.


Todo
----

    The key fucntion for this class - and project - is definitefly the shuffling. In the next 
versions I want to improve it to make it less "perfect", i.e. more human. I have in mind:

    - After splitting the deck in half, I beleive a person's choice of which half to start
    restacking from is dependable on such persons' dextry, i.e. left or right handness.
    Therefore, and given that roughly 10 percent of the world in left handed, I want to 
    implement a 10% chance of starting the restacking with the second half.
    - Stacking is not perfect, sometimes more than one card slips and gets stacked. I want
    to add a chance for that to happen. I am not sure of how frequently or how many at once,
    but it will judge the frequency and then the quantity.

@author: Luís Flávio
@version: 1.0

May 15th, 2019
Edmonton, AB
Canada
"""

# --- Constants
SUITS_FULL = ["Spades", "Hearts", "Clubs", "Diamonds"]
SUITS = ["S","H","C","D"]
NUMBERS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

class deck(object):

    def __init__(self):
        """ Initializes a new deck object, with cards in sequence and jokers at the end.
        """
        self.cards = []
        self.__init_deck__()

    def __init_deck__(self):
        """Adds the sequences and the jokers to the deck.
        """
        # Adding the sequences 
        for S in SUITS:
            for N in NUMBERS:
                self.cards.append(N+S)
        
        # Adding the jokers
        self.cards = self.cards + ["RJ","BJ"]

    def shuffle(self):
        """Shuffles the deck.

            Right now, it will only divide the deck in half and restacking the cards by picking the
        top one from each of the halfs one after the other. 

        """
        fhalf = self.cards[:len(self.cards)//2]
        shalf = self.cards[len(self.cards)//2:]

        to_shuffle = []
        for i,v in enumerate(fhalf):
            to_shuffle.append(fhalf[i])
            to_shuffle.append(shalf[i])
        
        self.cards = to_shuffle

