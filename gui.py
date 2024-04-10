import tkinter as tk
import random
# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()

        thewheel = tk.Canvas(self.mainWin)
        thewheel["width"] = 400
        thewheel["height"] = 400
        thewheel["bg"] = "pink"
        thewheel.grid(row=0, column=0)

        controlbar = tk.Frame(self.mainWin, bg = "lightblue", padx=10, pady=10)
        controlbar.grid(row=0, column=1)
        SPIN = tk.Button(controlbar)
        SPIN["text"] = "SPIN 🤑🤑🤑🤑🤑"
        SPIN.grid(row=1, column=1)

        stopspin = tk.Button(controlbar)
        stopspin["text"] = "STOP THAT WHEEL"
        stopspin.grid(row=2, column=1)


        saying = ['life is like gambling. i just need a little more money to keep going.', 'poopy', 'gamblers dont quit. they lose.']
        randsay = random.choice(saying)
        hashtagdeep = tk.Label(controlbar, text=randsay, font="Arial 10", wraplength=60, justify="center")
        hashtagdeep["width"] = 10
        hashtagdeep["height"] = 10
        hashtagdeep["bg"] = "red"
        hashtagdeep.grid(row=3, column=1)




    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
myGui = BasicGui()
myGui.run()