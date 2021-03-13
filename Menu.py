#It's quite long so I'd get comfy
from tkinter import *
import random
import reduce as red
import ReuseHackathonFunctions as reu
import autofill as rec
from inCouncil import *

#updating listbox for matrial


def updateMaterial(dataMat):
    #clear list box
    materialList.delete(0, END)
    for item in dataMat:
        materialList.insert(END, item)

#add the clicked item to list box


def filloutMaterial(event):
    #deletes current item in entry
    materialEntry.delete(0, END)
    #sets entry to item in list
    try:
        materialEntry.insert(0, materialList.get(materialList.curselection()))
    except:
        materialEntry.insert(0, materialList.get(ACTIVE))


#checks if item in listbox
def checkMaterial(event):
    #gets what is currently being typed
    typed = materialEntry.get()
    if typed == "":
        dataMat = materials
    else:
        dataMat = []
        for item in materials:
            if typed.lower() in item.lower():
                dataMat.append(item)
    #update listbox with selected
    updateMaterial(dataMat)
#updating listbox for matrial


def updateMaterial(dataMat):
    #clear list box
    materialList.delete(0, END)
    for item in dataMat:
        materialList.insert(END, item)

#add the clicked item to list box


def filloutMaterial(event):
    #deletes current item in entry
    materialEntry.delete(0, END)
    #sets entry to item in list
    try:
        materialEntry.insert(0, materialList.get(materialList.curselection()))
    except:
        materialEntry.insert(0, materialList.get(ACTIVE))


#checks if item in listbox
def checkMaterial(event):
    #gets what is currently being typed
    typed = materialEntry.get()
    if typed == "":
        dataMat = materials
    else:
        dataMat = []
        for item in materials:
            if typed.lower() in item.lower():
                dataMat.append(item)
    #update listbox with selected
    updateMaterial(dataMat)


#updating listbox for matrial
def updateMaterialItems(dataMatItem):
    #clear list box
    materialItemList.delete(0, END)
    for item in dataMatItem:
        materialItemList.insert(END, item)

#add the clicked item to list box


def filloutMaterialItem(event):
    #deletes current item in entry
    materialItemEntry.delete(0, END)
    #sets entry to item in list
    try:
        materialItemEntry.insert(0, materialItemList.get(
            materialItemList.curselection()))
    except:
        materialItemEntry.insert(0, materialItemList.get(ACTIVE))


#checks if item in listbox
def checkMaterialItem(event):
    #gets what is currently being typed
    typed = materialItemEntry.get()
    if typed == "":
        dataMat = materialItems
    else:
        dataMat = []
        for item in materialItems:
            if typed.lower() in item.lower():
                dataMat.append(item)
    #update listbox with selected
    updateMaterialItems(dataMat)


#updating listbox
def update(data):
    #clear list box
    councilList.delete(0, END)
    for item in data:
        councilList.insert(END, item)

#add the clicked item to list box


def fillout(event):
    #deletes current item in entry
    councilEntry.delete(0, END)
    #sets entry to item in list
    try:
        councilEntry.insert(0, councilList.get(councilList.curselection()))
    except:
        councilEntry.insert(0, councilList.get(ACTIVE))


#checks if item in listbox
def check(event):
    #gets what is currently being typed
    typed = councilEntry.get()
    if typed == "":
        data = councils
    else:
        data = []
        for item in councils:
            if typed.lower() in item.lower():
                data.append(item)
    #update listbox with selected
    update(data)


#defines what happens when button is clicked
def confirm():
    councilList.pack_forget()
    councilLabel.config(text=councilEntry.get())
    councilEntry.pack_forget()
    confirmBtn.pack_forget()
    myframe.pack_forget()

    materialLabel.pack()
    materialEntry.pack()
    materialList.pack()
    matframe.pack()
    confirmMatBtn.pack()

#defines what happens when button is clicked


def confirmMat():
    materialList.pack_forget()
    materialLabel.config(text=materialEntry.get())
    global materialItems
    materialItems += returnMaterialList(materialEntry.get())
    #updates list box
    updateMaterialItems(materialItems)
    materialEntry.pack_forget()
    matframe.pack_forget()
    confirmMatBtn.pack_forget()

    materialItemLabel.pack()
    materialItemEntry.pack()
    materialItemList.pack()
    matItemframe.pack()
    confirmMatItemBtn.pack()


def confirmMatItem():
    materialItemList.pack_forget()
    materialItemLabel.config(text=materialItemEntry.get())
    #if you can recycle or not
    global finalCouncil
    global finalItem
    finalCouncil = councilLabel.cget("text")
    finalItem = materialItemEntry.get()
    print(performLookUp(finalCouncil, finalItem))
    materialItemEntry.pack_forget()
    matItemframe.pack_forget()
    confirmMatItemBtn.pack_forget()

    if(performLookUp(finalCouncil, finalItem)):
        resultLbl.pack()
    else:
        findNearbyRCs()

def findNearbyRCs():
    noResultLbl.pack()
    noResultPCEntry.pack()
    noResultSearchBtn.pack()
    nearbyRCs.pack()

    nearbyRCs.delete(0, END)
    nearbyRCList = []
    startLocNew = noResultPCEntry.get()
    nearbyRCList = reu.locateNearbyRCs(startLocNew)
    for rc in nearbyRCList:
        nearbyRCs.insert(END, rc)
    print(nearbyRCList)



#function created for testing buttons


def clicked1():
    print("hello")


#uses Random to select a random fact from a load that are predefined
def randomFact(randomFactlb):
    randint = random.randint(1, 10)
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


def setRandomFact(msg, randomFactlb):
   randomFactlb.config(text=msg)

#fetches image of back button from directory


def getBackImage():
    return "C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newBack.png"


def reduceFunc(menuWidgets, window):

    for i in range(0, len(menuWidgets)):
        menuWidgets[i].pack_forget()

    #gets the first entries (the headers) of the reduce tips array.
    totalOptions = red.displayALternativesAndInfo()
    header = []
    for item in totalOptions:
        header.append(item[0])

    optionList = Listbox(window, width=50)
    explainLabel = Label(window, text='')

    def listboxFiller():
        for item in header:
            optionList.insert(END, item)

    previousText = ""
    textE = ""

    #Gets the reduce facts from reduce.py.
    def selected(event):
        textE = ""
        textArray = red.returnArray(optionList.get(optionList.curselection()))
        for item in textArray:
            textE += item + '\n\n'
        explainLabel.config(text=textE, anchor="n", borderwidth=4,
                            relief="solid", wraplength=400)

    #fills the optionlist box with the headers of totalOptions.
    listboxFiller()
    optionList.bind("<<ListboxSelect>>", selected)

    backImg = PhotoImage(file=getBackImage())

    back = Button(window, image=backImg, borderwidth=0,
                  command=lambda: revealMainMenu(menuWidgets, reduceWidgets, window))

    optionList.config(borderwidth=0, relief='solid', highlightbackground='#5C5B1B',
                      highlightcolor='#5C5B1B', highlightthickness=8, font=("courier", 10))
    optionList.pack(expand=True)

    explainLabel.config(width=60, height=8, font=("System", 10), borderwidth=4,
                        relief="solid", anchor='n', wraplength=400)
    explainLabel.pack(expand=True)

    back.config(bg='black', activebackground='black')
    back.pack(expand=True)

    #reduce widgets lets revealMainMenu know what widgets need to be hidden.
    reduceWidgets = [back, optionList, explainLabel]
    window.mainloop()


def reuseFunc(menuWidgets, window):
    for i in range(0, len(menuWidgets)):
        menuWidgets[i].pack_forget()

    totalOptions = reu.getTotalMaterials()

    optionList = Listbox(window, width=50)
    explainLabel = Label(window, text='')

    #Nearby charities, using Reuse Hackathon Functions:
    def searchForCharities():
        nearbyCharityList.delete(0, END)
        nearbyCharities = []
        startLoc = postcodeEntry.get()
        nearbyCharities = reu.locateNearbyCharities(startLoc)
        for charity in nearbyCharities:
            nearbyCharityList.insert(END, charity)
        print(nearbyCharities)

    postcodeExplain = Label(window, text="Enter your postcode to find nearby re-use charities: ",
                            width=130, font=("courier", 10), borderwidth=4, relief='solid')

    postcodeEntry = Entry(window, width=20, borderwidth=2, relief='raised')

    postcodeSearchBtn = Button(
        window, text="Search!", command=searchForCharities)

    nearbyCharityList = Listbox(window, width=90)
    nearbyCharityList.config(borderwidth=5, relief='sunken')

    def listboxFiller():
        for item in totalOptions:
            optionList.insert(END, item)

    #this part works very similarly to reduce.
    def selected(event):
        materialToSearch = optionList.get(optionList.curselection()).lower()
        textE = reu.displayReuseMethod(materialToSearch)
        explainLabel.config(text=textE, anchor="n",
                            borderwidth=4, relief="solid", wraplength=400)

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

    postcodeExplain.pack(expand=True)
    postcodeEntry.pack()

    postcodeSearchBtn.pack()

    nearbyCharityList.pack(expand=True)

    back.config(bg='black', activebackground='black')
    back.pack(expand=True)

    reduceWidgets = [back, optionList, explainLabel, postcodeEntry,
                     postcodeExplain, postcodeSearchBtn, nearbyCharityList]
    window.mainloop()


def recycleFunc(menuWidgets, window):
    for i in range(0, len(menuWidgets)):
        menuWidgets[i].pack_forget()

    backImg = PhotoImage(file=getBackImage())
    back = Button(window, image=backImg, borderwidth=0, command=lambda: revealMainMenu(menuWidgets, recycleWidgets, window))

    back.pack(padx=40)

    councilLabel.pack()
    councilEntry.pack()
    myframe.pack()
    councilList.pack()
    confirmBtn.pack()

    back.config(bg='black', activebackground='black')

    recycleWidgets = [back, councilLabel, councilEntry, myframe, councilList, confirmBtn,
                      materialLabel, materialEntry, matframe, materialList, confirmMatBtn, materialItemLabel,resultLbl,noResultLbl,noResultPCEntry,noResultSearchBtn,nearbyRCs]
    window.mainloop()


def revealMainMenu(menuWidgets, widgetsToHide, window):

    #hides every widget from previous menus.
    for i in range(0, len(widgetsToHide)):
        widgetsToHide[i].pack_forget()

    for i in range(0, len(menuWidgets)):
        if(menuWidgets[i] == 'randomFactlb' or menuWidgets[i] == 'ecopal'):
            menuWidgets[i].pack()
        else:
            menuWidgets[i].pack(expand=True)

    window.mainloop()


window = Tk()
window.title("EcoPal")
window.geometry("600x750")
window.config(bg='lightgreen')


reduceImg = PhotoImage(
    file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newReduce.png")
reuseImg = PhotoImage(
    file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newReuse.png")
recycleImg = PhotoImage(
    file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newRecycle.png")
backgroundimg = PhotoImage(
    file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newBackgroundImg.png")
ecopalImg = PhotoImage(
    file="C:\\Users\\matth\\OneDrive\\Desktop\\Hackathon Ideas\\EcoPal\\images\\newEcoPalImage.png")

backgroundLabel = Label(window, image=backgroundimg)
ecopal = Label(window, image=ecopalImg)
reduce = Button(window, image=reduceImg, borderwidth=0,
                command=lambda: reduceFunc(menuWidgets, window))
reuse = Button(window, image=reuseImg, borderwidth=0,
               command=lambda: reuseFunc(menuWidgets, window))
recycle = Button(window, image=recycleImg, borderwidth=0,
                 command=lambda: recycleFunc(menuWidgets, window))
randomFactlb = Label(
    window, text="11% of the world's population are currently vulnerable to climate change impacts")

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
randomFactlb.config(height=1, width=100, bg='#5C5B1B',
                    font=factFont, fg='white')

randomFact(randomFactlb)
menuWidgets = [ecopal, reduce, reuse, recycle, randomFactlb]


#make widget
#label for the council
councilLabel = Label(window, text="Enter council name")
#create council entry
councilEntry = Entry(window, width=250)
#add scrolling
myframe = Frame(window)
myScroll = Scrollbar(myframe, orient=VERTICAL)

#creating a list box to autofill from
councilList = Listbox(myframe, width=250, height=4,
                      yscrollcommand=myScroll.set)
myScroll.config(command=councilList.yview)
myScroll.pack(side=RIGHT, fill=Y)
#array of all the councils
councils = returnCouncilList()

#updates list box
update(councils)

#when an item is selected from the list
councilList.bind("<<ListboxSelect>>", fillout)

#when a key is released so somthing is typed
councilEntry.bind("<KeyRelease>", check)

#creating way for user to selection
confirmBtn = Button(window, text="Confirm", command=confirm)

#label for the matrial type
materialLabel = Label(window, text="Enter material Type")
#create material type entry
materialEntry = Entry(window, width=250)
matframe = Frame(window)
matScroll = Scrollbar(matframe, orient=VERTICAL)

#creating a list box to autofill from
materialList = Listbox(matframe, width=250, height=4,
                       yscrollcommand=matScroll.set)
matScroll.config(command=materialList.yview)
matScroll.pack(side=RIGHT, fill=Y)
#array of all the material type
materials = returnMatType()

resultLbl = Label(window, text="Your local council accepts this item!")
resultLbl.config(font=("courier", 11))

noResultLbl = Label(window,text="Your council does not accept this item. Enter you postcode to find nearby centres:")
noResultLbl.config(font=("courier", 8))

noResultPCEntry = Entry(window)
noResultPCEntry.config( width=20, borderwidth=2, relief='raised')

noResultSearchBtn = Button(window,text = "Search!",command = findNearbyRCs)

nearbyRCs = Listbox(window, width = 90)
nearbyRCs.config(borderwidth=5, relief='sunken')

#updates list box
updateMaterial(materials)

#when an item is selected from the list
materialList.bind("<<ListboxSelect>>", filloutMaterial)

#when a key is released so somthing is typed
materialEntry.bind("<KeyRelease>", checkMaterial)
#creating way for user to material type selection
confirmMatBtn = Button(window, text="Confirm", command=confirmMat)
#label for the matrial
materialItemLabel = Label(window, text="Enter material name")
#create material entry
materialItemEntry = Entry(window, width=250)
matItemframe = Frame(window)
matItemScroll = Scrollbar(matItemframe, orient=VERTICAL)

#creating a list box to autofill from
materialItemList = Listbox(matItemframe, width=250,
                           height=4, yscrollcommand=matItemScroll.set)
matItemScroll.config(command=materialItemList.yview)
matItemScroll.pack(side=RIGHT, fill=Y)
materialItems = []  # returnMaterialList(councilLabel.get())

#when an item is selected from the list
materialItemList.bind("<<ListboxSelect>>", filloutMaterialItem)

#when a key is released so somthing is typed
materialItemEntry.bind("<KeyRelease>", checkMaterialItem)
confirmMatItemBtn = Button(window, text="Confirm", command=confirmMatItem)

#packing
#displays the council
councilLabel.pack()
councilEntry.pack()
myframe.pack()
councilList.pack()
confirmBtn.pack()
materialLabel.pack()

resultLbl.pack()
noResultLbl.pack()
noResultPCEntry.pack()
noResultSearchBtn.pack()
nearbyRCs.pack()

materialEntry.pack()
matframe.pack()
materialList.pack()
confirmMatBtn.pack()
materialItemLabel.pack()
materialItemEntry.pack()
matItemframe.pack()
materialItemList.pack()
confirmMatItemBtn.pack()

#forgeting
councilLabel.pack_forget()
councilEntry.pack_forget()
myframe.pack_forget()
councilList.pack_forget()
confirmBtn.pack_forget()
resultLbl.pack_forget()
noResultLbl.pack_forget()
noResultPCEntry.pack_forget()
noResultSearchBtn.pack_forget()
nearbyRCs.pack_forget()


#remove unneeded widgets
materialLabel.pack_forget()
materialEntry.pack_forget()
matframe.pack_forget()
materialList.pack_forget()
confirmMatBtn.pack_forget()
materialItemLabel.pack_forget()
materialItemEntry.pack_forget()
matItemframe.pack_forget()
materialItemList.pack_forget()
confirmMatItemBtn.pack_forget()

#variabls to store final result
finalCouncil = ""
finalItem = ""

#mainMenu()
window.mainloop()
