import random

optionsForSlotMachine = { 1: "A",
                         4: "B",
                         3: "C",
                         2: "D",
                          5: "the",
                          6: 7,
                          7: "Neopet"}

key = 0
value = 0
for x in range(5):
    value = random.random()
if value <= .2:
    print(optionsForSlotMachine.get(1))
elif .2 < value <= .4:
    print(optionsForSlotMachine.get(2))
elif .4 < value <= .6:
    print(optionsForSlotMachine.get(3))
elif .6 < value <= .7:
    print(optionsForSlotMachine.get(4))
elif .7 <value <= .8:
    print(optionsForSlotMachine.get(5))
elif.8 <value <= .97:
    print(optionsForSlotMachine.get(6))
elif .97 < value <= 1:
    print(optionsForSlotMachine.get(7))
# When stop button is pressed
#




