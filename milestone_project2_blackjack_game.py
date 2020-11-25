# Milestone Project 2 - Blackjack Game
"""
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:

You must use OOP and classes in some portion of your game.
You can not just use functions in your game.
Use classes to help you define the Deck and the Player's hand.

To play a hand of Blackjack the following steps must be followed:

1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand.
The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again

Playing Cards
A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs)
and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck.
Jacks, Queens and Kings all have a rank of 10.
Aces have a rank of either 11 or 1 as needed to reach 21 without busting.
As a starting point in your program, you may want to assign variables to store a list of suits, ranks,
and then use a dictionary to map ranks to values.
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    """
    A Card object really only needs two attributes: suit and rank.
    Consider adding a __str__ method that, when asked to print a Card, returns a string in the form "Two of Hearts"
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    """
    Here we might store 52 card objects in a list that can later be shuffled.
    First, though, we need to instantiate all 52 unique card objects and add them to our list.
    In addition to an __init__ method we'll want to add methods to shuffle our deck,
    and to deal out cards during game play.
    """
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    """
    In addition to holding Card objects dealt from the Deck,
    the Hand class may be used to calculate the value of those cards using the values dictionary defined above.
    It may also need to adjust for the value of Aces when appropriate.
    """
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)          # card passed in from Deck.deal() --> single Card(suit, rank)
        self.value += values[card.rank]  # We use the rank of the card to call the value in the dictionary.
        if card.rank == 'Ace':           # Track aces
            self.aces += 1

    def adjust_for_ace(self):
        """
        If total value is > 21 and I still have an ace,
        than change my ace to be a 1 instead of an 11.
        We use the self.aces integer number as a boolean.
        0 is going to be False and 1,2,3... are going to be True.
        :return:
        """
        while self.value > 21 and self.aces:
            self.value -= 10  # We adjust the ace. We reduce the value from 11 to 1. (11-10 = 1)
            self.aces -= 1    # We subtract 1 for the ace count.


class Chips:
    """
    In addition to decks of cards and hands,
    we need to keep track of a Player's starting chips, bets, and ongoing winnings.
    """
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    """
    Function for taking bets.
    Check that a Player's bet can be covered by their available chips.
    :param chips: The amount of chips the player is going to bet.
    :return:
    """
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, your bet can not exceed {chips.total}')
            else:
                break


def hit(deck, hand):
    """
    Function for taking hits.
    Either player can take hits until they bust.
    This function will be called during game play anytime a Player requests a hit,
    or a Dealer's hand is less than 17.
    We also could do:
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    :param deck:
    :param hand:
    :return:
    """
    hand.add_card(deck.deal())  # Grabs a single card for the deck and added to the hand.
    hand.adjust_for_ace()       # Checks for an ace adjustment.


def hit_or_stand(deck, hand):
    """
    Function prompting the Player to Hit or Stand.
    This function should accept the deck and the player's hand as arguments,
    and assign playing as a global variable.
    :param deck:
    :param hand:
    :return:
    """
    global playing  # to control an upcoming while loop

    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[1].lower() == 's':
            print('Player stands. Dealer is playing.')
            playing = False
        else:
            print("Sorry, please enter 'h' or 's' only!")
            continue
        break


def show_some(player, dealer):
    """
    Function to display cards.
    When the game starts, and after each time Player takes a card,
    the dealer's first card is hidden and all of Player's cards are visible.
    :param player:
    :param dealer:
    :return:
    """
    print("\nDEALER'S HAND:")
    print(' <card hidden>')
    print('', dealer.cards[1])
    print("\nPLAYER'S HAND:", *player.cards, sep='\n ')


def show_all(player, dealer):
    """
    Function to display cards.
    At the end of the hand all cards are shown, and you may want to show each hand's total value.
    :param player:
    :param dealer:
    :return:
    """
    print("\nDEALER'S HAND:", *dealer.cards, sep='\n ')
    print("DEALER'S HAND =", dealer.value)
    print("\nPLAYER'S HAND:", *player.cards, sep='\n ')
    print("PLAYER'S HAND =", player.value)


def player_busts(player, dealer, chips):
    """
    Functions to handle end of game scenarios.
    :param player:
    :param dealer:
    :param chips:
    :return:
    """
    print('Player busts!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    """
    Functions to handle end of game scenarios.
    :param player:
    :param dealer:
    :param chips:
    :return:
    """
    print('Player wins!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    """
    Functions to handle end of game scenarios.
    :param player:
    :param dealer:
    :param chips:
    :return:
    """
    print('Dealer busts!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    """
    Functions to handle end of game scenarios.
    :param player:
    :param dealer:
    :param chips:
    :return:
    """
    print('Dealer wins!')
    chips.lose_bet()


def push(player, dealer):
    """
    Functions to handle end of game scenarios.
    :param player:
    :param dealer:
    :return:
    """
    print('Dealer and Player tie! It is a push.')


while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n'
          'Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print(f"Player's winnings stand at {player_chips.total}")

        # Ask to play again
        new_game = input("Would you like to play another hand?\nEnter Yes or No:")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thank's for playing!")
            break
    break
