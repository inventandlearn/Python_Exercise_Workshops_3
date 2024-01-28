import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []
while diamonds:
    user_input = input("Press enter to pick a card or hit Q then enter to quit: ")
    if user_input == "Q":
        break
    elif user_input == "":
        random_card = random.choice(diamonds)
        hand.append(random_card)
        diamonds.remove(random_card)
        print("Your hand: " + str(hand))
        print("Remaining cards: " + str(diamonds))
        print("")
        print("")
if not diamonds:
    print("There are no more cards to pick from! ")


