import tkinter as tk
import random

import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk


# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        # ----- Callbacks for Calculations Stuff -----
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
        def payout(bet, rolled_value1,rolled_value2,rolled_value3,legend_value):
            if rolled_value1 == rolled_value2 == rolled_value3:
                cash_multipler = legend_value.get(rolled_value1)
                return bet * cash_multipler
            else:
                return bet * 0
        def stop(bet,legend,legend_values):
            image1 = spin_calculations(legend)
            image2 = spin_calculations(legend)
            image3 = spin_calculations(legend)
            # stopspin
            # set each image to the corrusponding image
            winnings = payout(bet,image1,image2,image3,legend_values)
            return winnings #This will eventually change to update the payout tab and the total credit tab






        # ----- Each Widget -----
        wheelpluslegend = tk.Frame(self.mainWin, bg='gray', padx=10, pady=10)
        wheelpluslegend.grid(row=0, column=0)

        thewheel = tk.Canvas(wheelpluslegend)
        thewheel["width"] = 400
        thewheel["height"] = 400
        thewheel["bg"] = "pink"
        thewheel.grid(row=0, column=0)


        legend = tk.Label(wheelpluslegend, text='lalalalalal this is a legend its so cool', font="Arial 10", wraplength=400, justify="center")
        legend.grid(row=1, column=0)

        controlbar = tk.Frame(self.mainWin, bg = "lightblue", padx=10, pady=10)
        controlbar.grid(row=0, column=1)
        SPIN = tk.Button(controlbar)
        SPIN["text"] = "SPIN"
        SPIN.grid(row=1, column=1)


        stopspin = tk.Button(controlbar)
        stopspin["text"] = "STOP THAT WHEEL"
        stopspin.grid(row=2, column=1)


        saying = ['life is like gambling. i just need a little more money to keep going.', 'Sonic says "I love Gambling"', 'gamblers dont quit. they lose.',
                  'Dont quit! youre about to make it big!', 'I love Gambling', 'gambling...mmmmm', 'hello amin alhashim', 'youre gonna win this one i know it']
        randsay = random.choice(saying)
        # SPIN["command"] = self.changesaying
        hashtagdeep = tk.Label(controlbar, text=randsay, font="Arial 10", wraplength=60, justify="center")
        hashtagdeep["width"] = 10
        hashtagdeep["height"] = 10
        hashtagdeep["bg"] = "red"
        hashtagdeep.grid(row=3, column=1)

        self.bagpipesImg = ImageTk.PhotoImage(file="Images/bagpipesResized.jpg")
        self.diamondImg = ImageTk.PhotoImage(file="Images/diamondResized.jpg")

        self.bagpipes = thewheel.create_image(100, 100, image=self.bagpipesImg)  # Credit to the page for helping me with finding and implementing images in the tkinter module  (https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter)
        self.diamond = thewheel.create_image(100, 300, image=self.diamondImg)

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
myGui = BasicGui()
myGui.run()