from tkinter import *
from in_council import *

root = Tk()
root.title('Autofill council')
root.geometry("300x300")


#updating listbox for matrial
def updateMaterial(dataMat):
    #clear list box
    materialList.delete(0,END)
    for item in dataMat:
        materialList.insert(END,item)

#add the clicked item to list box
def filloutMaterial(event):
    #deletes current item in entry
    materialEntry.delete(0,END)
    #sets entry to item in list
    try:
        materialEntry.insert(0, materialList.get(materialList.curselection()))
    except:
        materialEntry.insert(0, materialList.get(ACTIVE))


#checks if item in listbox  
def checkMaterial(event):
    #gets what is currently being typed
    typed  = materialEntry.get()
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
    materialList.delete(0,END)
    for item in dataMat:
        materialList.insert(END,item)

#add the clicked item to list box
def filloutMaterial(event):
    #deletes current item in entry
    materialEntry.delete(0,END)
    #sets entry to item in list
    try:
        materialEntry.insert(0, materialList.get(materialList.curselection()))
    except:
        materialEntry.insert(0, materialList.get(ACTIVE))


#checks if item in listbox  
def checkMaterial(event):
    #gets what is currently being typed
    typed  = materialEntry.get()
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
    materialItemList.delete(0,END)
    for item in dataMatItem:
        materialItemList.insert(END,item)

#add the clicked item to list box
def filloutMaterialItem(event):
    #deletes current item in entry
    materialItemEntry.delete(0,END)
    #sets entry to item in list
    try:
        materialItemEntry.insert(0, materialItemList.get(materialItemList.curselection()))
    except:
        materialItemEntry.insert(0, materialItemList.get(ACTIVE))


#checks if item in listbox  
def checkMaterialItem(event):
    #gets what is currently being typed
    typed  = materialItemEntry.get()
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
    councilList.delete(0,END)
    for item in data:
        councilList.insert(END,item)

#add the clicked item to list box
def fillout(event):
    #deletes current item in entry
    councilEntry.delete(0,END)
    #sets entry to item in list
    try:
        councilEntry.insert(0, councilList.get(councilList.curselection()))
    except:
        councilEntry.insert(0, councilList.get(ACTIVE))


#checks if item in listbox  
def check(event):
    #gets what is currently being typed
    typed  = councilEntry.get()
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
    councilLabel.config(text =councilEntry.get())
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
    materialLabel.config(text =materialEntry.get())
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
    materialItemLabel.config(text =materialItemEntry.get())
    #if you can recycle or not
    global finalCouncil
    global finalItem
    finalCouncil = councilLabel.cget("text")
    finalItem = materialItemEntry.get()
    print(performLookUp(finalCouncil, finalItem))
    materialItemEntry.pack_forget()
    matItemframe.pack_forget()
    confirmMatItemBtn.pack_forget()


#autofill for council
#label for the council
councilLabel = Label(root, text = "Enter council name")
#displays the council
councilLabel.pack()


#create council entry
councilEntry = Entry(root, width =250)
councilEntry.pack()

#add scrolling
myframe = Frame(root)
myScroll = Scrollbar(myframe, orient=VERTICAL)

#creating a list box to autofill from
councilList = Listbox(myframe, width =250, height = 4, yscrollcommand = myScroll.set)
myScroll.config(command = councilList.yview)
myScroll.pack(side = RIGHT, fill = Y)
myframe.pack()
councilList.pack()

#array of all the councils
councils = returnCouncilList()

#updates list box
update(councils)

#when an item is selected from the list
councilList.bind("<<ListboxSelect>>", fillout)

#when a key is released so somthing is typed
councilEntry.bind("<KeyRelease>", check)

#creating way for user to selection
confirmBtn = Button(root, text = "Confirm", command = confirm)
confirmBtn.pack() 

#autofill for material type
#label for the matrial type
materialLabel = Label(root, text = "Enter material Type")
#displays the material type
materialLabel.pack()


#create material type entry
materialEntry = Entry(root, width =250)
materialEntry.pack()

#add scrolling
matframe = Frame(root)
matScroll = Scrollbar(matframe, orient=VERTICAL)

#creating a list box to autofill from
materialList = Listbox(matframe, width =250, height = 4, yscrollcommand = matScroll.set)
matScroll.config(command = materialList.yview)
matScroll.pack(side = RIGHT, fill = Y)
matframe.pack()
materialList.pack()

#array of all the material type
materials = returnMatType()

#updates list box
updateMaterial(materials)

#when an item is selected from the list
materialList.bind("<<ListboxSelect>>", filloutMaterial)

#when a key is released so somthing is typed
materialEntry.bind("<KeyRelease>", checkMaterial)

#remove unneeded widgets
materialList.pack_forget()
materialEntry.pack_forget()
materialLabel.pack_forget()
matframe.pack_forget()


#creating way for user to material type selection
confirmMatBtn = Button(root, text = "Confirm", command = confirmMat)
confirmMatBtn.pack() 
confirmMatBtn.pack_forget()

#autofill for material
#label for the matrial 
materialItemLabel = Label(root, text = "Enter material name")
#displays the material
materialItemLabel.pack()


#create material entry
materialItemEntry = Entry(root, width =250)
materialItemEntry.pack()

#add scrolling
matItemframe = Frame(root)
matItemScroll = Scrollbar(matItemframe, orient=VERTICAL)

#creating a list box to autofill from
materialItemList = Listbox(matItemframe, width =250, height = 4, yscrollcommand = matItemScroll.set)
matItemScroll.config(command = materialItemList.yview)
matItemScroll.pack(side = RIGHT, fill = Y)
matItemframe.pack()
materialItemList.pack()

#array of all the materials
materialItems = []#returnMaterialList(councilLabel.get())



#when an item is selected from the list
materialItemList.bind("<<ListboxSelect>>", filloutMaterialItem)

#when a key is released so somthing is typed
materialItemEntry.bind("<KeyRelease>", checkMaterialItem)

#remove unneeded widgets
materialItemList.pack_forget()
materialItemEntry.pack_forget()
materialItemLabel.pack_forget()
matItemframe.pack_forget()

#creating way for user to material type selection
confirmMatItemBtn = Button(root, text = "Confirm", command = confirmMatItem)
confirmMatItemBtn.pack() 
confirmMatItemBtn.pack_forget()


#variabls to store final result
finalCouncil =""
finalItem = ""
root.mainloop()
