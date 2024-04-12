import tkinter as tk
import random

from util.display_helper import *
from util.imageTools import *
# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()

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
        SPIN["command"] = self.changesaying
        hashtagdeep = tk.Label(controlbar, text=randsay, font="Arial 10", wraplength=60, justify="center")
        hashtagdeep["width"] = 10
        hashtagdeep["height"] = 10
        hashtagdeep["bg"] = "red"
        hashtagdeep.grid(row=3, column=1)

        bagpipes = tk.PhotoImage(file='Images/dupreHall.png')
        bagpiesGui = tk.Label(self.mainWin, image=bagpipes)
        bagpiesGui.grid(row=1, column=1)


    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
myGui = BasicGui()
myGui.run()