from tkinter import *
import random


def clicked1():
    print("hello")

def randomFact():
    randint = random.randint(1,10)
    if randint == 1:
        setRandomFact("As of May 2020, the concentration of CO2 is the highest in human history.")
    elif randint == 2:
        setRandomFact("The 5 warmest years in human history are between 1880-2019")
    elif randint == 3:
        setRandomFact("11% of all emissions are from deforestation")
    elif randint == 4:
        setRandomFact("Nature-based solutions only recieve 3% of all climate funding")
    elif randint == 5:
        setRandomFact("Cows and sheep are responsible for 37% of methane")
    elif randint == 6:
        setRandomFact("11% of the world's population are currently vulnerable to climate change impacts")
    elif randint == 7:
        setRandomFact("You save 13,000 litres of water /KG of beef you don't eat")
    elif randint == 8:
        setRandomFact("800,000 hectares of mangrove swamp. At this rate, they could dissapear within the next century")
    elif randint == 9:
        setRandomFact("The 20 warmest years on record have been in the past 22 years")
    elif randint == 10:
        setRandomFact("If you don't eat a packet of crisps, someone won't die")

def setRandomFact(msg):
   randomFactlb.config(text=msg)

window = Tk()
window.title("EcoPal")
window.geometry("600x750")
window.config(bg='lightgreen')

reduceImg = PhotoImage(file="reduce.png")
reuseImg = PhotoImage(file="reuse.png")
recycleImg = PhotoImage(file="recycle.png")
backgroundimg = PhotoImage(file="backgroundimg.png")
ecopalImg = PhotoImage(file="EcoPal.png")

backgroundLabel = Label(window,image = backgroundimg)
ecopal = Label(window,image=ecopalImg)
reduce = Button(window, image=reduceImg,borderwidth=0, command=clicked1)
reuse = Button(window, image = reuseImg,borderwidth=0, command = clicked1)
recycle = Button(window, image=recycleImg, borderwidth=0, command=clicked1)
randomFactlb = Label(window, text="11% of the world's population are currently vulnerable to climate change impacts")

titleFont = ('courier',40,'bold')
factFont = ('times',13)


backgroundLabel.place(x=0,y=0, relwidth=1, relheight=1)
ecopal.pack()
ecopal.config( bg='#009FFF')
reduce.pack(expand=True)
reduce.config(bg='#009FFF', activebackground='#009FFF')
reuse.pack(expand=True)
reuse.config(bg='#009FFF', activebackground='#009FFF')
recycle.pack(expand=True)
recycle.config(bg='#009FFF', activebackground='#009FFF')
randomFactlb.pack()
randomFactlb.config(height=2, width=100, bg='#564800', font=factFont)

randomFact()
window.mainloop()
