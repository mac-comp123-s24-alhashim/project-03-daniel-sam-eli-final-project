import random

optionsForSlotMachine = {1: "Trash",
                         4: "Bagpipes",
                         3: "Loch Ness Monster",
                         2: "Diamond",
                         5: "Cherry",
                         6: "Dupre",
                         7: "Jackpot"}

key = 0
value = 0
rolled_values = []
for x in range(3):
    for x in range(5):
        value = random.random()
    if value <= .2:
        rolled_values.append(optionsForSlotMachine.get(1))
    elif .2 < value <= .4:
        rolled_values.append(optionsForSlotMachine.get(2))
    elif .4 < value <= .6:
        rolled_values.append(optionsForSlotMachine.get(3))
    elif .6 < value <= .7:
        rolled_values.append(optionsForSlotMachine.get(4))
    elif .7 < value <= .8:
        rolled_values.append(optionsForSlotMachine.get(5))
    elif .8 < value <= .95:
        rolled_values.append(optionsForSlotMachine.get(6))
    elif .95 < value <= 1:
        rolled_values.append(optionsForSlotMachine.get(7))
# When stop button is pressed
print(rolled_values)
