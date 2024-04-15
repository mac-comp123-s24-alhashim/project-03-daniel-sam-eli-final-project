import random
def spin_calculations(legend):
    rolled_value = 0
    for i in range(5):
        value = random.random()
        if value <= .2:
            rolled_value = legend.get(1)
        elif .2 < value <= .4:
            rolled_value = legend.get(2)
        elif .4 < value <= .6:
            rolled_value = legend.get(3)
        elif .6 < value <= .7:
            rolled_value = legend.get(4)
        elif .7 < value <= .8:
            rolled_value = legend.get(5)
        elif .8 < value <= .95:
            rolled_value = legend.get(6)
        elif .95 < value <= 1:
            rolled_value = legend.get(7)
        print(rolled_value)
        return rolled_value


def payout(bet, rolled_value1, rolled_value2, rolled_value3, legend_value):
    if rolled_value1 == rolled_value2 == rolled_value3:
        cash_multipler = legend_value.get(rolled_value1)
        money =  int(bet * cash_multipler)
        return money
    elif rolled_value1 == rolled_value2:
        cash_multipler = legend_value.get(rolled_value2)
        money = int(bet * cash_multipler/2)
        return money
    elif rolled_value2 == rolled_value3:
        cash_multipler = legend_value.get(rolled_value2)
        money = int(bet * cash_multipler/2)
        return money
    elif rolled_value3 == rolled_value1:
        cash_multipler = legend_value.get(rolled_value2)
        money = int(bet* cash_multipler/2)
        return money
    else:
        return bet * 0


def stop(bet, legend, legend_values):
    image1 = spin_calculations(legend)
    image2 = spin_calculations(legend)
    image3 = spin_calculations(legend)
    # stopspin
    # set each image to the corrusponding image
    winnings = payout(bet, image1, image2, image3, legend_values)
    return winnings  # This will eventually change to update the payout tab and the total credit tab

def main():
    optionsForSlotMachine = {1: "Trash",
                             4: "Bagpipes",
                             3: "Loch Ness Monster",
                             2: "Apple",
                             5: "Diamond",
                             6: "Dupre",
                             7: "Jackpot"}
    SlotMachine_value = {"Trash": .5,
                             "Bagpipes":1.5,
                             "Loch Ness Monster": 2,
                              "Apple": 3,
                              "Diamond": 4,
                              "Dupre": 1,
                             "Jackpot":7}
    # user_bet = input("please enter number")
    # user_bet = int(user_bet)
    print(stop(3,optionsForSlotMachine,SlotMachine_value))

main()
