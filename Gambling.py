import random
def start_spin(credit):
    print("Your Current Wallet is  " + str(credit))
    while True:
        bet = input("How many coins will you bet: ")
        if int(bet) > credit:
            print("Try Again, You're Too Poor")
        else:
            return int(bet)
            break

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


def stop(bet, legend, legend_values, credit):
    image1 = spin_calculations(legend)
    image2 = spin_calculations(legend)
    image3 = spin_calculations(legend)
    # stopspin
    # set each image to the corrusponding image
    winnings = payout(bet, image1, image2, image3, legend_values)
    return "Payout = " + str(winnings), "Total Money = " +str((credit - bet + winnings)), (credit - bet + winnings)  # This will eventually change to update the payout tab and the total credit tab

def main():
    casino_credit = 100
    optionsForSlotMachine = {1: "Trash",
                             4: "Bagpipes",
                             3: "Loch Ness Monster",
                             2: "Apple",
                             5: "Diamond",
                             6: "Dupre",
                             7: "Jackpot"}
    SlotMachine_value = {"Trash": .5,
                             "Bagpipes":1.5,
                             "Loch Ness Monster": 3,
                              "Apple": 4,
                              "Diamond": 5,
                              "Dupre": 2,
                             "Jackpot": 100}
    for i in range(3):
        bet = start_spin(casino_credit)
        big_shot = stop(bet,optionsForSlotMachine,SlotMachine_value, casino_credit)
        print(big_shot[0:2])
        casino_credit = big_shot[2]
    print("Your total is " + str(casino_credit))
    if casino_credit <= 100000000000000000000000000000:
        print("Man, you suck at gambling")

