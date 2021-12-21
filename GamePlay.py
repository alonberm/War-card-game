# GamePlay.py
# Alon
# 1/1/2021
# game play of war, behind the scenes

import random # import random module

class Card:
    # represents a card
    def __init__(self, value, suit):
        self.value = value # value of the card (str)
        self.suit = suit # suit of the card (str)
    #end __init__()
    def __str__(self):
        # prints value of card
        namesOfCards = ['Jack', 'Queen', 'King', 'Ace']
        if self.value <= 10:
            result = f'{self.value}'
        else:
            result = f'{namesOfCards[self.value-11]}'
        #end if
        return result
    #end __str__
#end Card

class CardGroup:
# represents an arbitrary group of cards...might be a standard deck
    def __init__(self, cards=[]):
        self.cards = cards # card list (list of Card)
    # end __init__()

    def nextCard(self):
        # removes the first card from the list and return it
        # param: none
        # return the next cards (Card)
        return self.cards.pop(0)
    # end nextCard()

    def hasCards(self):
        # returns True or False depending on if there are any cards left in the list
        # param: none
        # return: True or false (bool)
        return len(self.cards) > 0
    # end has Cards()

    def shuffle(self):
        # shuffles the list
        # param: none
        # return null
        random.shuffle(self.cards) # shuffles the list of cards
        return
    # end shuffle()
#end CardGroup

class StandardDeck(CardGroup):
# 52-card deck
    def __init__(self):
        self.cards = [] # initilize list of cards (list)
        for s in ['hearts', 'diamonds', 'clubs', 'spades']: # iterate through all possibilities of suit and value
            for v in range(2,15):
                self.cards.append(Card(v, s)) # append a card to the list
            # end for
        # end for
    #end __init__()
#end StandardDeck
        
class WarGame():
    # represents the game of war
    def __init__(self):
        deck = StandardDeck() # create standard deck of cards (StandardDeck)
        deck.shuffle() # shuffle the deck

        self.deck1 = CardGroup(deck.cards[:26]) # set half the deck to deck1 (CardGroup)
        self.deck2 = CardGroup(deck.cards[26:]) # set the other half to deck2 (CardGroup)

        self.warDeck = [] # initialize war deck (list)
        self.exit = False # initialize exit indicating end of game (bool)
    # end __init__()

    def nextRound(self):
        # plays the next round when 2 cards are flipped
        # param: none
        # return null
        
        self.card1 = self.deck1.nextCard() # gets next card from deck1
        self.card2 = self.deck2.nextCard() # gets next card from deck2
        
        if self.card1.value > self.card2.value: # if card1 is higher than card2
            self.player1Higher() # player1 gets cards
        # end if
        elif self.card2.value > self.card1.value: # if card2 is higher than card1
            self.player2Higher()  # player 2 gets cards
        # end elif
        else: # tie
            self.war() # war
        # end else
        
        self.exit = self.endGame() # set exit to true when a player runs out of cards
        return
    # end nextRound()
    
    def player1Higher(self):
        # appends cards to deck1
        # param: none
        # return: null
        # append cards to deck1
        self.deck1.cards.append(self.card1) 
        self.deck1.cards.append(self.card2)
        self.deck1.cards.extend(self.warDeck) # extend war deck to deck1
        self.warDeck[:] = [] # empty war deck
        return
    # end player1Higher()

    def player2Higher(self):
        # appends cards to deck2
        # param: none
        # return: null
        # append cards to deck2
        self.deck2.cards.append(self.card1)
        self.deck2.cards.append(self.card2)
        self.deck2.cards.extend(self.warDeck) # extend warDeck to deck2
        self.warDeck[:] = [] # empty war deck
        return
    # end player2Higher()

    def war(self):
        # appends right amount of cards to war deck during war
        # param: none
        # return: null
        # append cards to war deck
        self.warDeck.append(self.card1)
        self.warDeck.append(self.card2)
        minLength = min(len(self.deck1.cards), len(self.deck2.cards)) # get the smallest length of the 2 decks

        if minLength == 2: # if smallest deck has 2 cards
            self.warDeck.append(self.deck1.nextCard()) # append next card from deck1 to warDeck
            self.warDeck.append(self.deck2.nextCard()) # append next card from deck2 to warDeck
        # end if
        elif minLength == 3: # if smallest deck has 3 cards
            for i in range(2): # iterate twice
                self.warDeck.append(self.deck1.nextCard()) # append next card from deck1 to warDeck
                self.warDeck.append(self.deck2.nextCard()) # append next card from deck2 to warDeck
            # end for
        # end elif
        elif minLength > 3: # if smallest deck has more than 3 cards
            for i in range(3): # iterate three times
                self.warDeck.append(self.deck1.nextCard()) # append next card from deck1 to warDeck
                self.warDeck.append(self.deck2.nextCard()) # append next card from deck2 to warDeck
            # end for
        # end elif
        return
    # end war()

    def endGame(self):
        # check if a player won
        # param: none
        # return: value for exit (bool)
        exit = False # initialize exit to false (bool)
        if not(self.deck1.hasCards()) or not(self.deck2.hasCards()):
            exit = True
        # end if
        return exit
    # end endGame()
# end WarGame
