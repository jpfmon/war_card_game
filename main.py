from random import shuffle

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        cards_list = f"\n\n {len(self.cards)} Cards in {self.name}:\n "
        for item in self.cards:
            cards_list = cards_list + item.__str__() + " | "
        return cards_list

    def receive_card(self, card):
        self.cards.append(card)

    def shows_card(self):
        card_showed = self.cards.pop(0)
        return card_showed


class Deck:
    def __init__(self):
        self.cards = []

    def __str__(self):
        cards_list = "\n\nCards in Deck: \n"
        for item in self.cards:
            cards_list = cards_list + item.__str__() + " | "
        return cards_list

    def shuffle_cards(self):
        for item in suits:
            for it in ranks:
                self.cards.append(Card(item, it))
        # for item in self.cards:
        # print(item.__str__(),end=" / ")
        # print(" \n\n SHUFFLE \n\n")
        shuffle(self.cards)
        # for item in self.cards:
        # print(item.__str__(), end=" / ")

    def deal_one(self, player1, player2):
        # if to_player == True, card goes to player1, else to player2
        to_player = True
        shuffle(self.cards)
        while len(self.cards) > 0:
            handed_card = self.cards.pop()
            if (to_player):
                player1.receive_card(handed_card)
                to_player = False
            else:
                player2.receive_card(handed_card)
                to_player = True


player1 = Player("Player 1")
player2 = Player("Player 2")
deck = Deck()

# print("Player 1 cards: \n")
print(player1)
# print("Player 2 cards: \n")
print(player2)
# print("Deck cards: \n")
# print(deck)
print("**********************************")

deck.shuffle_cards()
# print(deck)
deck.deal_one(player1, player2)

# print("Player 1 cards:")
print(player1)
# print("Player 2 cards:")
print(player2)
# print("Deck cards:")
# print(deck)

while True:
    print("**********************************")
    # turn = int(input("\nNext turn? \nYes - 1 \nStop - 2\n"))
    turn = 1
    length_p1_cards = len(player1.cards)
    length_p2_cards = len(player2.cards)

    if turn == 1 and length_p1_cards > 0 and length_p2_cards > 0:
        card_player1 = player1.shows_card()
        print(card_player1)
        card_player2 = player2.shows_card()
        print(card_player2)

        if card_player1.rank > card_player2.rank:
            player1.cards.append(card_player1)
            player1.cards.append(card_player2)
        elif card_player1.rank < card_player2.rank:
            player2.cards.append(card_player2)
            player2.cards.append(card_player1)

        else:
            print("Same rank value")
            cards1 = [card_player1]
            cards2 = [card_player2]
            if len(player1.cards) > 3 and len(player2.cards) > 3:
                for i in range(1, 4):
                    cards1.append(player1.cards.pop(0))
                    cards2.append(player2.cards.pop(0))
                    i += 1
            else:
                limit_range = 0
                if len(player1.cards) > len(player2.cards):
                    limit_range = len(player2.cards)
                else:
                    limit_range = len(player1.cards)

                for i in range(1, limit_range):
                    cards1.append(player1.cards.pop(0))
                    cards2.append(player2.cards.pop(0))
                    i += 1

            sum_cards1 = 0
            sum_cards2 = 0

            for item in cards1:
                sum_cards1 = sum_cards1 + item.rank
            for item in cards2:
                sum_cards2 = sum_cards2 + item.rank
            print(f"Sum_cards1 : {sum_cards1}")
            print(f"Sum_cards2 : {sum_cards2}")
            # Just to pause for a moment
            # texto = input("Compare sums")
            print("Comparing...")
            if sum_cards1 < sum_cards2:
                player2.cards.extend(cards1)
                player2.cards.extend(cards2)
                # for item in cards1:
                #     player2.cards.append(item)
                # for item in cards2:
                #     player2.cards.append(item)
            else:
                player1.cards.extend(cards2)
                player1.cards.extend(cards1)
                # for item in cards2:
                #     player1.cards.append(item)
                # for item in cards1:
                #     player1.cards.append(item)
    else:
        print("Ends game")
        break
    print(player1)
    print(player2)
    # print(length_p1_cards)
    # print(length_p2_cards)
    if length_p1_cards > 1:
        print("Player 1 wins")
    else:
        print("Player 2 wins")