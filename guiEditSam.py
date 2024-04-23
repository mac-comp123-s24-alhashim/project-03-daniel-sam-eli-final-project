import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk

import os
#------Helper Function
def ask_bet(credit):
    while True:
        bet = simpledialog.askinteger("Your current credit is" + str(credit), "what would you like to bet")
        if int(bet) <= credit:
            return int(bet)
            break
        else:
            messagebox.showerror("Try Again",
                                 "You don't have enough credit")


# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        # ----- Callbacks for Calculations Stuff -----

        def spin_calculations(self, legend):
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

        def payout(self, bet, rolled_value1, rolled_value2, rolled_value3, legend_value):
            if rolled_value1 == rolled_value2 == rolled_value3:
                cash_multipler = legend_value.get(rolled_value1)
                return bet * cash_multipler
            else:
                return bet * 0

        def stop(self, bet, legend, legend_values, credit):
            image1 = self.spin_calculations(legend)
            image2 = self.spin_calculations(legend)
            image3 = self.spin_calculations(legend)
            # stopspin
            # set each image to the corrusponding image
            winnings = self.payout(bet, image1, image2, image3, legend_values)
            credit = (credit - bet + winnings)
            return winnings, credit

        def start_spin():
           print(ask_bet(casino_credit))

        self.mainWin = tk.Tk()





        nameList = os.listdir("Images")  # Credit to this page for this method and the prof for mentioning it: https://www.geeksforgeeks.org/python-list-files-in-a-directory/

        self.imgList = []

        for picName in nameList:
            openedImage = Image.open("Images/" + picName)
            pic = ImageTk.PhotoImage(openedImage)
            self.imgList.append(pic)

        wheelpluslegend = tk.Frame(self.mainWin, bg='gray', padx=10, pady=10)
        wheelpluslegend.grid(row=0, column=0)

        thewheel = tk.Canvas(wheelpluslegend)
        wheelheight = 300
        wheelwidth = 400
        thewheel["width"] = wheelwidth
        thewheel["height"] = wheelheight
        thewheel["bg"] = "pink"
        thewheel.grid(row=0, column=0, padx=25, pady=50)

        thewheel.create_image(75, 150, image=random.choice(self.imgList))
        thewheel.create_image(200, 150, image=random.choice(self.imgList))
        thewheel.create_image(350, 150, image=random.choice(self.imgList))

        legend = tk.Label(wheelpluslegend, text='lalalalalal this is a legend its so cool', font="Arial 10",
                          wraplength=400, justify="center")
        legend.grid(row=1, column=0)


        controlbar = tk.Frame(self.mainWin, bg="lightblue", padx=10, pady=10)
        controlbar.grid(row=0, column=1)

        payoutlabel = tk.Label(controlbar)
        payoutlabel.grid(row=0, column=1)
        payoutlabel["text"] = "Payout:", winnings

        whattosay = "Credit:" , casino_credit
        moneystatus = tk.Label(controlbar)
        moneystatus.grid(row=1, column=1)
        moneystatus["text"] = whattosay

        SPIN = tk.Button(controlbar)
        SPIN['command'] = start_spin
        SPIN["text"] = "SPIN"
        SPIN.grid(row=2, column=1)




        stopspin = tk.Button(controlbar)
        stopspin["text"] = "STOP THAT WHEEL"
        stopspin.grid(row=3, column=1)

        saying = ['life is like gambling. i just need a little more money to keep going.',
                  'Sonic says "I love Gambling"', 'gamblers dont quit. they lose.',
                  'Dont quit! youre about to make it big!', 'I love Gambling', 'gambling...mmmmm',
                  'hello amin alhashim', 'youre gonna win this one i know it']
        randsay = random.choice(saying)
        # SPIN["command"] = self.changesaying
        hashtagdeep = tk.Label(controlbar, text=randsay, font="Arial 10", wraplength=60, justify="center")
        hashtagdeep["width"] = 10
        hashtagdeep["height"] = 10
        hashtagdeep["bg"] = "red"
        hashtagdeep.grid(row=4, column=1)


    # def rotateImages(self):

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
casino_credit = 100
winnings = 0
myGui = BasicGui()
myGui.run()