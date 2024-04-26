"""
Authors: Sam Jackson, Eli Poll, and Daniel Quintero (dquinter@macalester.edu)

Our program creates a slot machine by asking the user how many credits they want to bet and spinning images that are
attached to values. When the user stops it, these images will determine their payout.
"""

import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog

import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk

import os
import time

# Helper Functions

def ask_bet(credit):
    """
    This function takes in the amount of credits the user has and asks them how many credits they want to bet, returning
    that as a int variable to be used with other functions.
    """
    while True:
        bet = simpledialog.askinteger("Betting Window",
                                      "Your current credit is " + str(credit) + ", what would you like to bet")
        if int(bet) <= credit:
            return int(bet)
        else:
            messagebox.showerror("Try Again",
                                 "You don't have enough credit")



def spin_calculations(legend):
    """
    This function takes in the legend dictionary within the init and uses a random number generator and probability
    to return a variable which is set to one of the legend keys.
    """
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
        if .95 < value <= 1:
            rolled_value = legend.get(7)
        return rolled_value


def payout(bet, rolled_value1, rolled_value2, rolled_value3, legend_value):
    """
    This function takes in the number of credits the user bet, three of the variables that determine the value
    based on legend, and the legend value itself, and returns the payout the user gets based on if conditionals.
    """
    if rolled_value1 == rolled_value2 == rolled_value3:
        cash_multipler = legend_value.get(rolled_value1)
        money = int(bet * cash_multipler)
        if rolled_value1 == "Jackpot":
            for i in range(10):
                messagebox.showinfo("JACKPOT",
                                    "JACKPOT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return money
    elif rolled_value1 == rolled_value2:
        cash_multipler = legend_value.get(rolled_value2)
        money = int(bet * cash_multipler / 2)
        return money
    elif rolled_value2 == rolled_value3:
        cash_multipler = legend_value.get(rolled_value2)
        money = int(bet * cash_multipler / 2)
        return money
    elif rolled_value3 == rolled_value1:
        cash_multipler = legend_value.get(rolled_value3)
        money = int(bet * cash_multipler / 2)
        return money
    else:
        return bet * 0



def stop(bet, legend, legend_values, credit, image_values, block, row1, row2, row3):
    """
    This function takes in the bet, the legend canvas, the values of the legend, the amount of credit the user has,
    the images attached to the values, as well as the entire block of the images and three row for each of the images, and
    returns the payout, the remaining the credit, and the new images when the user hits the stop button.
    """
    image1 = spin_calculations(legend)
    image2 = spin_calculations(legend)
    image3 = spin_calculations(legend)
    block.delete(row1)
    block.delete(row2)
    block.delete(row3)
    new_row1 = block.create_image(75, 150, image=image_values[image1])
    new_row2 = block.create_image(200, 150, image=image_values[image2])
    new_row3 = block.create_image(350, 150, image=image_values[image3])
    winnings = payout(bet, image1, image2, image3, legend_values)
    credit = (credit - bet + winnings)
    return winnings, credit, new_row1, new_row2, new_row3


# ----- GUI class and methods -----
"""
A class that sets up all the objects and methods to create the GUI that takes in the helper functions from above.
"""
class BasicGui:
    """
    A function that takes no inputs and creates the GUI, returning the GUI with all the additions below.
    """
    def __init__(self):

        self.mainWin = tk.Tk()
        self.mainWin.title("The Lucky Loch Casino")
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
        self.user_bet = 0
        self.spin_button = "not pressed"

        name_list = os.listdir(
            "Images")  # Credit to this page for this method and the prof for mentioning it: https://www.geeksforgeeks.org/python-list-files-in-a-directory/

        self.imgList = []

        for picName in name_list:
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

        wheel_plus_legend = tk.Frame(self.mainWin, padx=10, pady=10)
        wheel_plus_legend.grid(row=0, column=0)

        self.the_wheel = tk.Canvas(wheel_plus_legend)
        wheel_height = 300
        wheel_width = 400
        self.the_wheel["width"] = wheel_width
        self.the_wheel["height"] = wheel_height
        self.the_wheel["bg"] = "darkgreen"
        self.the_wheel.grid(row=0, column=0, padx=25, pady=15)

        self.img1 = self.the_wheel.create_image(75, 150, image=random.choice(self.imgList))
        self.img2 = self.the_wheel.create_image(200, 150, image=random.choice(self.imgList))
        self.img3 = self.the_wheel.create_image(350, 150, image=random.choice(self.imgList))

        legend = tk.Label(wheel_plus_legend,
                          text='Cafe Mac = 0.5    Bagpipes = 1.5  Loch Ness Monster = 3   Apple = 4   Diamond = 5 Dupre = 2   Jackpot = 100'
                               '                                           Rolling doubles of any multiplier will only give you half of the multiplier!',
                          font="Arial 10",
                          wraplength=400, justify="center", bg="light gray", borderwidth=2, relief="solid")
        legend.grid(row=1, column=0, pady=10)

        control_bar = tk.Frame(self.mainWin, borderwidth=1, relief="solid", padx=10, pady=10, bg="light gray")
        control_bar.grid(row=0, column=1)

        self.payout_label = tk.Label(control_bar)
        self.payout_label.grid(row=0, column=1)
        self.payout_label["text"] = "Payout:", self.winnings

        what_to_say = "Credit:", self.casino_credit
        self.money_status = tk.Label(control_bar)
        self.money_status.grid(row=1, column=1, pady=3)
        self.money_status["text"] = what_to_say

        SPIN = tk.Button(control_bar)
        SPIN["text"] = "SPIN"
        SPIN["command"] = self.start_spin
        SPIN.grid(row=2, column=1, pady=3)

        stopButton = tk.Button(control_bar)
        stopButton["text"] = "STOP THAT WHEEL"
        stopButton['command'] = self.stop_spin
        stopButton.grid(row=3, column=1)

        saying = ['life is like gambling. i just need a little more money to keep going.',
                  'Sonic says "I love Gambling"', 'gamblers dont quit. they lose.',
                  'Dont quit! you are about to make it big!', 'I love Gambling', 'gambling...mmmmm',
                  'hello amin alhashim', 'you are gonna win this one i know it', 'gambler? i hardly know her!',
                  '1 2 3 4 you should try and gamble more',
                  'the early gambler gets the jackpot -A Wise Man', 'the next one is a jackpot. I just know it!!!']
        rand_say = random.choice(saying)

        hashtag_deep = tk.Label(control_bar, text=rand_say, font="Arial 10", wraplength=60, justify="center",
                                borderwidth=2, relief="solid", bg="light gray")
        hashtag_deep["width"] = 10
        hashtag_deep["height"] = 10
        hashtag_deep.grid(row=4, column=1, pady=10)

        # ----- Callbacks for Calculations Stuff -----

    def run(self):
        """
        A callback function that takes no inputs or has no returns and runs the GUI, or the main window with the
        additions above.
        """
        self.mainWin.mainloop()

    def rotateImages(self):
        """
        A callback function that takes no inputs and has no returns which rotates the images from the folder at a rate
        of 0.2 seconds and updates the canvas where they are located.
        """
        while self.spin_button == "pressed":
            self.the_wheel.delete(self.img1)
            self.the_wheel.delete(self.img2)
            self.the_wheel.delete(self.img3)
            self.img1 = self.the_wheel.create_image(75, 150, image=random.choice(self.imgList))
            self.img2 = self.the_wheel.create_image(200, 150, image=random.choice(self.imgList))
            self.img3 = self.the_wheel.create_image(350, 150, image=random.choice(self.imgList))
            self.the_wheel.update()
            time.sleep(0.2)

    def start_spin(self):
        """
        A callback function that takes no inputs or returns and adjusts the GUI above when the spin button is pressed
        and ensures that the user cannot click the button again while spinning.
        """
        if self.spin_button == "not pressed":
            self.user_bet = ask_bet(self.casino_credit)
            self.spin_button = "pressed"
            self.rotateImages()
        else:
            messagebox.showerror("Error", "Already Spinning")

    def stop_spin(self):
        """
        A callback that takes no inputs and has no returns which calculates the winnings, and remaining credit
        the user has after they click the "stop spin" button
        """
        if self.spin_button == "pressed":
            winning_array = stop(self.user_bet, self.optionsForSlotMachine, self.SlotMachine_value, self.casino_credit,
                                 self.imgValues, self.the_wheel, self.img1, self.img2, self.img3)
            self.winnings = winning_array[0]
            self.casino_credit = winning_array[1]
            self.img1 = winning_array[2]
            self.img2 = winning_array[3]
            self.img3 = winning_array[4]
            self.spin_button = "not pressed"
            self.payout_label["text"] = "Payout:", self.winnings
            self.money_status["text"] = "Credit:", self.casino_credit
            if self.casino_credit == 0:
                messagebox.showinfo("You Lost!!!!", "You have no credit left, come back when you have money")
                self.mainWin.destroy()
        else:
            messagebox.showerror("Error", "nothing to stop")


# ----- Main program -----
myGui = BasicGui()
myGui.run()
