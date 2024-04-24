import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog

import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk

import os
# Helper Functions
def ask_bet(credit):
    while True:
        bet = simpledialog.askinteger("Betting Window","Your current credit is " + str(credit) + ", what would you like to bet")
        if int(bet) <= credit:
            return int(bet)
            break
        else:
            messagebox.showerror("Try Again",
                                 "You don't have enough credit")
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
        return rolled_value


def payout(bet, rolled_value1, rolled_value2, rolled_value3, legend_value):
    if rolled_value1 == rolled_value2 == rolled_value3:
        cash_multipler = legend_value.get(rolled_value1)
        money = int(bet * cash_multipler)
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
        cash_multipler = legend_value.get(rolled_value3)
        money = int(bet* cash_multipler/2)
        return money
    else:
        return bet * 0


def stop(bet, legend, legend_values, credit, image_values, block, row1,row2,row3):
    image1 = spin_calculations(legend)
    image2 = spin_calculations(legend)
    image3 = spin_calculations(legend)
    block.delete(row1)
    block.delete(row2)
    block.delete(row3)
    row1 = block.create_image(75, 150, image= image_values[image1])
    row2 = block.create_image(200, 150, image= image_values[image2])
    row3 = block.create_image(350, 150, image= image_values[image3])
    winnings = payout(bet, image1, image2, image3, legend_values)
    credit = (credit - bet + winnings)
    return winnings, credit

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.optionsForSlotMachine = {1: "Cafe Mac",
                                      4: "Bagpipes",
                                      3: "Loch Ness Monster",
                                      2: "Apple",
                                      5: "Diamond",
                                      6: "Dupre",
                                      7: "Jackpot"}
        self.SlotMachine_value = {"Cafe Mac": .5,
                                  "Bagpipes": 1.5,
                                  "Loch Ness Monster": 3,
                                  "Apple": 4,
                                  "Diamond": 5,
                                  "Dupre": 2,
                                  "Jackpot": 100}

        self.casino_credit = 100
        self.winnings = 0
        self.user_Bet = 0
        self.spin_button = "not pressed"

        nameList = os.listdir("Images")  # Credit to this page for this method and the prof for mentioning it: https://www.geeksforgeeks.org/python-list-files-in-a-directory/

        self.imgList = []

        for picName in nameList:
            openedImage = Image.open("Images/" + picName)
            pic = ImageTk.PhotoImage(openedImage)
            self.imgList.append(pic)
        self.imgValues = {"Cafe Mac": self.imgList[6],
                          "Bagpipes": self.imgList[0],
                          "Loch Ness Monster": self.imgList[4],
                          "Apple": self.imgList[3],
                          "Diamond": self.imgList[1],
                          "Dupre": self.imgList[2],
                          "Jackpot": self.imgList[5]}

        wheelpluslegend = tk.Frame(self.mainWin, padx=10, pady=10)
        wheelpluslegend.grid(row=0, column=0)

        self.thewheel = tk.Canvas(wheelpluslegend)
        wheelheight = 300
        wheelwidth = 400
        self.thewheel["width"] = wheelwidth
        self.thewheel["height"] = wheelheight
        self.thewheel["bg"] = "darkgreen"
        self.thewheel.grid(row=0, column=0, padx=25, pady=15)

        self.img1 = self.thewheel.create_image(75, 150, image=random.choice(self.imgList))
        self.img2 = self.thewheel.create_image(200, 150, image=random.choice(self.imgList))
        self.img3 = self.thewheel.create_image(350, 150, image=random.choice(self.imgList))

        legend = tk.Label(wheelpluslegend,
                          text='Cafe Mac = 0.5    Bagpipes = 1.5  Loch Ness Monster = 3   Apple = 4   Diamond = 5 Dupre = 2   Jackpot = 100'
                               '                                           Rolling doubles of any multiplier will only give you half of the multiplier!',
                          font="Arial 10",
                          wraplength=400, justify="center", bg="lightgray", borderwidth=2, relief="solid")
        legend.grid(row=1, column=0, pady=10)

        controlbar = tk.Frame(self.mainWin, borderwidth=1, relief="solid", padx=10, pady=10, bg="lightgray")
        controlbar.grid(row=0, column=1)

        self.payoutlabel = tk.Label(controlbar)
        self.payoutlabel.grid(row=0, column=1)
        self.payoutlabel["text"] = "Payout:", self.winnings

        whattosay = "Credit:", self.casino_credit
        self.moneystatus = tk.Label(controlbar)
        self.moneystatus.grid(row=1, column=1, pady=3)
        self.moneystatus["text"] = whattosay

        SPIN = tk.Button(controlbar)
        SPIN["text"] = "SPIN"
        SPIN["command"] = self.start_spin
        SPIN.grid(row=2, column=1, pady=3)

        stopButton = tk.Button(controlbar)
        stopButton["text"] = "STOP THAT WHEEL"
        stopButton['command'] = self.stop_spin
        stopButton.grid(row=3, column=1)

        saying = ['life is like gambling. i just need a little more money to keep going.',
                  'Sonic says "I love Gambling"', 'gamblers dont quit. they lose.',
                  'Dont quit! youre about to make it big!', 'I love Gambling', 'gambling...mmmmm',
                  'hello amin alhashim', 'youre gonna win this one i know it', 'gambler? i hardly know her!', '1 2 3 4 you should try and gamble more',
                  'the early gambler gets the jackpot -A Wise Man', 'the next one is a jackpot. I just know it!!!']
        randsay = random.choice(saying)
        # SPIN["command"] = self.changesaying
        hashtagdeep = tk.Label(controlbar, text=randsay, font="Arial 10", wraplength=60, justify="center",
                               borderwidth=2, relief="solid", bg="lightgray")
        hashtagdeep["width"] = 10
        hashtagdeep["height"] = 10
        hashtagdeep.grid(row=4, column=1, pady=10)


        # ----- Callbacks for Calculations Stuff -----
    # def rotateImages(self):

    def run(self):
        self.mainWin.mainloop()

    def start_spin(self):
        if self.spin_button == "not pressed":
            self.user_Bet = ask_bet(self.casino_credit)
            self.spin_button = "pressed"
        else:
            messagebox.showerror("Error", "Already Spinning")

    def stop_spin(self):
        if self.spin_button == "pressed":
            winning_array = stop(self.user_Bet, self.optionsForSlotMachine, self.SlotMachine_value, self.casino_credit,
                                 self.imgValues, self.thewheel, self.img1, self.img2, self.img3)
            self.winnings = winning_array[0]
            self.casino_credit = winning_array[1]
            self.spin_button = "not pressed"
            self.payoutlabel["text"] = "Payout:", self.winnings
            self.moneystatus["text"] = "Credit:", self.casino_credit
            if self.casino_credit == 0:
                messagebox.showinfo("You Lost!!!!", "You have no credit left, Try again to make money")
                self.casino_credit = 100
                self.moneystatus["text"] = "Credit:", self.casino_credit
        else:
            messagebox.showerror("Error", "nothing to stop")


# ----- Main program -----
myGui = BasicGui()
myGui.run()