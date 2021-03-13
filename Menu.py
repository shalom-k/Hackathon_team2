from tkinter import *
import random
import reduce as red
import ReuseHackathonFunctions as reu

#function created for testing buttons
def clicked1():
    print("hello")


#uses Random to select a random fact from a load that are predefined
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
            "Mangrove swamps are on track to dissapear next century.", randomFactlb)
    elif randint == 9:
        setRandomFact(
            "The 20 warmest years on record have been in the past 22 years.", randomFactlb)
    elif randint == 10:
        setRandomFact(
            "If you don't eat a packet of crisps, someone won't die.", randomFactlb)

#this function knows what the randomFactlb is, and sets it's text to a given message
def setRandomFact(msg,randomFactlb):
   randomFactlb.config(text=msg)

def getBackImage():
    return "C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newBack.png"

def reduceFunc(menuWidgets,window):

    for i in range(0,len(menuWidgets)):
        menuWidgets[i].pack_forget()


    totalOptions = red.displayALternativesAndInfo()
    header = []
    for item in totalOptions:
        header.append(item[0])

    optionList = Listbox(window,width=50)
    explainLabel = Label(window,text='')
    

    def listboxFiller():
        for item in header:
            optionList.insert(END,item)

    previousText = ""
    textE = ""

    def selected(event):
        textE = ""
        textArray = red.returnArray(optionList.get( optionList.curselection()))
        for item in textArray:
            textE += item +'\n\n'
        explainLabel.config(text=textE, anchor="n", borderwidth=4,
                            relief="solid", wraplength = 400)
        


    listboxFiller()
    optionList.bind("<<ListboxSelect>>",selected)

    backImg = PhotoImage(file=getBackImage())

    back = Button(window,image=backImg,borderwidth=0, command=lambda:revealMainMenu(menuWidgets,reduceWidgets,window))

    optionList.config(borderwidth=0, relief='solid', highlightbackground='#5C5B1B',
                      highlightcolor='#5C5B1B', highlightthickness=8, font = ("courier",10))
    optionList.pack(expand=True)

    explainLabel.config(width=60, height=8, font=("System", 10), borderwidth=4,
                        relief="solid", anchor='n', wraplength=400)
    explainLabel.pack(expand=True)

    back.config(bg='black', activebackground='black')
    back.pack(expand=True)

    reduceWidgets = [back,optionList,explainLabel]
    window.mainloop()


def reuseFunc(menuWidgets, window):
    for i in range(0, len(menuWidgets)):
        menuWidgets[i].pack_forget()

    totalOptions = reu.getTotalMaterials()

    optionList = Listbox(window, width=50)
    explainLabel = Label(window, text='')

    #Nearby charities:
    def searchForCharities():
        nearbyCharities = []
        startLoc = postcodeEntry.get()
        nearbyCharities = reu.locateNearbyCharities(startLoc)
        for charity in nearbyCharities:
            nearbyCharityList.insert(END,charity)
        print(nearbyCharities)

    postcodeExplain = Label(window,text="Enter your postcode to find nearby re-use charities: ",width = 130, font=("courier",10),borderwidth=4,relief='solid')

    postcodeEntry = Entry(window,width=20,borderwidth=2,relief='raised')

    postcodeSearchBtn = Button(window,text = "Search!",command = searchForCharities)

    nearbyCharityList = Listbox(window,width=90)
    nearbyCharityList.config(borderwidth=5,relief='sunken')

    

    def listboxFiller():
        for item in totalOptions:
            optionList.insert(END, item)


    def selected(event):
        materialToSearch = optionList.get(optionList.curselection()).lower()
        textE = reu.displayReuseMethod(materialToSearch)
        explainLabel.config(text=textE, anchor="n", borderwidth=4,relief="solid", wraplength=400)

    listboxFiller()
    optionList.bind("<<ListboxSelect>>", selected)

    backImg = PhotoImage(file=getBackImage())

    back = Button(window, image=backImg, borderwidth=0,
                  command=lambda: revealMainMenu(menuWidgets, reduceWidgets, window))

    optionList.config(borderwidth=0, relief='solid', highlightbackground='#5C5B1B',
                      highlightcolor='#5C5B1B', highlightthickness=8, font=("courier", 10))
    optionList.pack()

    explainLabel.config(width=60, height=8, font=("System", 10), borderwidth=4,
                        relief="solid", anchor='n', wraplength=400)
    explainLabel.pack()

    postcodeExplain.pack(expand = True)
    postcodeEntry.pack()

    postcodeSearchBtn.pack()

    nearbyCharityList.pack(expand=True)

    back.config(bg='black', activebackground='black')
    back.pack(expand = True)


    reduceWidgets = [back, optionList, explainLabel,postcodeEntry,postcodeExplain,postcodeSearchBtn,nearbyCharityList]
    window.mainloop()


def recycleFunc(menuWidgets, window):
    for i in range(0, len(menuWidgets)):
        menuWidgets[i].pack_forget()

    backImg = PhotoImage(
        file=getBackImage())
    back = Button(window, image=backImg, borderwidth=0, command=lambda: revealMainMenu(menuWidgets, recycleWidgets, window))

    back.pack()
    back.config(bg='black', activebackground='black')

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

    reduceImg = PhotoImage(file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newReduce.png")
    reuseImg = PhotoImage(file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newReuse.png")
    recycleImg = PhotoImage(file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newRecycle.png")
    backgroundimg = PhotoImage(file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newBackgroundImg.png")
    ecopalImg = PhotoImage(file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newEcoPalImage.png")

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
    ecopal.config(bg='black')
    reduce.pack(expand=True)
    reduce.config(bg='black', activebackground='black')
    reuse.pack(expand=True)
    reuse.config(bg='black', activebackground='black')
    recycle.pack(expand=True)
    recycle.config(bg='black', activebackground='black')
    randomFactlb.pack()
    randomFactlb.config(height=1, width=100, bg='#5C5B1B', font=factFont,fg='white')

    randomFact(randomFactlb)
    menuWidgets = [ecopal, reduce, reuse, recycle, randomFactlb]
    window.mainloop()

mainMenu()

