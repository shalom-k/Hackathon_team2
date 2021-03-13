from tkinter import *
import random


def clicked1():
    print("hello")


def randomFact(randomFactlb):
    randint = random.randint(1,10)
    if randint == 1:
        setRandomFact(
            "As of May 2020, the concentration of CO2 is the highest in human history.", randomFactlb)
    elif randint == 2:
        setRandomFact(
            "The 5 warmest years in human history are between 1880-2019", randomFactlb)
    elif randint == 3:
        setRandomFact(
            "11% of all emissions are from deforestation.", randomFactlb)
    elif randint == 4:
        setRandomFact(
            "Nature-based solutions only recieve 3% of all climate funding.", randomFactlb)
    elif randint == 5:
        setRandomFact(
            "Cows and sheep are responsible for 37% of methane.", randomFactlb)
    elif randint == 6:
        setRandomFact(
            "11% of the world's population are currently vulnerable to climate change impacts.", randomFactlb)
    elif randint == 7:
        setRandomFact(
            "You save 13,000 litres of water per KG of beef you don't eat.", randomFactlb)
    elif randint == 8:
        setRandomFact(
            "800,000 hectares of mangrove swamp. They could dissapear next century.", randomFactlb)
    elif randint == 9:
        setRandomFact(
            "The 20 warmest years on record have been in the past 22 years.", randomFactlb)
    elif randint == 10:
        setRandomFact(
            "If you don't eat a packet of crisps, someone won't die.", randomFactlb)

def setRandomFact(msg,randomFactlb):
   randomFactlb.config(text=msg)



def reduceFunc(menuWidgets,window):
    for i in range(0,len(menuWidgets)):
        menuWidgets[i].pack_forget()

    backImg = PhotoImage(file = "Back.png")
    back = Button(window,image=backImg,borderwidth=0, command=lambda:revealMainMenu(menuWidgets,reduceWidgets,window))

    back.pack()
    back.config(bg='#009FFF', activebackground='#009FFF')

    reduceWidgets = [back]
    window.mainloop()


def reuseFunc(menuWidgets, window):
    for i in range(0, len(menuWidgets)):
        menuWidgets[i].pack_forget()

    backImg = PhotoImage(file="Back.png")
    back = Button(window, image=backImg, borderwidth=0, command=lambda: revealMainMenu(menuWidgets, reuseWidgets, window))

    back.pack()
    back.config(bg='#009FFF', activebackground='#009FFF')

    reuseWidgets = [back]
    window.mainloop()


def recycleFunc(menuWidgets, window):
    for i in range(0, len(menuWidgets)):
        menuWidgets[i].pack_forget()

    backImg = PhotoImage(file="Back.png")
    back = Button(window, image=backImg, borderwidth=0, command=lambda: revealMainMenu(menuWidgets, recycleWidgets, window))

    back.pack()
    back.config(bg='#009FFF', activebackground='#009FFF')

    recycleWidgets = [back]
    window.mainloop()

def revealMainMenu(menuWidgets,widgetsToHide,window):
    for i in range(0,len(widgetsToHide)):
        widgetsToHide[i].pack_forget()

    for i in range(0,len(menuWidgets)):
        if(menuWidgets[i] == 'randomFactlb' or menuWidgets[i] == 'ecopal'):
            menuWidgets[i].pack()
        else:
            menuWidgets[i].pack(expand=True)

    window.mainloop()

def mainMenu():
    window = Tk()
    window.title("EcoPal")
    window.geometry("600x750")
    window.config(bg='lightgreen')

    reduceImg = PhotoImage(file="reduce.png")
    reuseImg = PhotoImage(file="reuse.png")
    recycleImg = PhotoImage(file="recycle.png")
    backgroundimg = PhotoImage(file="backgroundimg.png")
    ecopalImg = PhotoImage(file="EcoPal.png")

    backgroundLabel = Label(window, image=backgroundimg)
    ecopal = Label(window, image=ecopalImg)
    reduce = Button(window, image=reduceImg, borderwidth=0, command=lambda:reduceFunc(menuWidgets,window))
    reuse = Button(window, image=reuseImg, borderwidth=0, command=lambda:reuseFunc(menuWidgets,window))
    recycle = Button(window, image=recycleImg, borderwidth=0, command=lambda:recycleFunc(menuWidgets,window))
    randomFactlb = Label(window, text="11% of the world's population are currently vulnerable to climate change impacts")

    titleFont = ('courier', 40, 'bold')
    factFont = ('times', 13)

    backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
    ecopal.pack()
    ecopal.config(bg='#009FFF')
    reduce.pack(expand=True)
    reduce.config(bg='#009FFF', activebackground='#009FFF')
    reuse.pack(expand=True)
    reuse.config(bg='#009FFF', activebackground='#009FFF')
    recycle.pack(expand=True)
    recycle.config(bg='#009FFF', activebackground='#009FFF')
    randomFactlb.pack(expand=True)
    randomFactlb.config(height=1, width=100, bg='#564800', font=factFont)

    randomFact(randomFactlb)
    menuWidgets = [ecopal, reduce, reuse, recycle, randomFactlb]
    window.mainloop()

mainMenu()

