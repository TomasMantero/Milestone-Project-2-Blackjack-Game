# Milestone Project 2 - Blackjack Game

![Python](https://img.shields.io/badge/Python-3.7.6-blue) ![License](https://img.shields.io/badge/License-Apache%202.0-orange) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-green)

In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

- You need to create a simple text-based BlackJack game
- The game needs to have one player versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount.
- You need to keep track of the player's total money.
- You need to alert the player of wins, losses, or busts, etc...

And most importantly:

- You must use OOP and classes in some portion of your game.
- You can not just use functions in your game.
- Use classes to help you define the Deck and the Player's hand.

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
A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting. As a starting point in your program, you may want to assign variables to store a list of suits, ranks, and then use a dictionary to map ranks to values.

## Context

Blackjack, is the American member of a global family of banking games known as Twenty-One, whose relatives include the British game of Pontoon and the European game. It is a comparing card game between one or more players and a dealer, where each player in turn competes against the dealer. Players do not compete against each other. It is played with one or more decks of 52 cards, and is the most widely played casino banking game in the world.

## License

This Notebook has been released under the Apache 2.0 open source license.
