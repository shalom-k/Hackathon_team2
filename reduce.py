popularProducts = [[]]

#create a 2d array to store the information for reduce

popularProducts[0].append("Water Bottle")
popularProducts[0].append("Instead of buying a single use plastic bottle, buy a reusable water bottle if you can.")
popularProducts[0].append("You could always try drinking tap water. It's not as bad as you think!")


popularProducts.append([])
popularProducts[1].append("Toilet Paper")
popularProducts[1].append(
    "Instead of using toilet papers from trees, try bamboo toilet paper such as bumboo!")
popularProducts[1].append("Bamboo is the fastest growing plant and only takes 3-5 years to mature. It also supports rural development and gives farmers a sustainable income.")

popularProducts.append([])
popularProducts[2].append("Clothing")
popularProducts[2].append(
    "Buy second hand items. This limits CO2 emissions, the use of pesticides and fertilizers.")
popularProducts[2].append("Billions of litres of water are also saved from being used to make new clothes.")

popularProducts.append([])
popularProducts[3].append("Single Use Plastic Packaging")
popularProducts[3].append("Visit stores which encourage you to refill your own glass containers instead of buying new plastic packaging each time." +
                          "You can also consider buying items in bulk.")
popularProducts[3].append("This reduces the number of plastic waste produced.")

popularProducts.append([])
popularProducts[4].append("Single Use Cleaning Products")
popularProducts[4].append("Instead of buying single use cleaning products and throwing out the plastic bottle, try cleaning tablets. ")
popularProducts[4].append("This reduces the number of plastic waste produced.")

popularProducts.append([])
popularProducts[5].append("New Things")
popularProducts[5].append(
    "Instead of buying new things, consider the items you already own in your home. Think of whether you really need that item.")
popularProducts[5].append(
    "This reduces the energy used to build those items and Co2 to ship them, and ensures old items dont go to waste.")

popularProducts.append([])
popularProducts[6].append("Food")
popularProducts[6].append(
    "Compost your own food waste and use it as a fertiliser.")
popularProducts[6].append(
    "This reduces food waste sent to landfill, and ensures food waste is productively used.")

popularProducts.append([])
popularProducts[7].append("Tea")
popularProducts[7].append("Try drinking loose leaf tea!")
popularProducts[7].append("Plastic accounts for roughly 25% of the teabag. By switching to loose leaf, you will reduce the amount of plastic ending up in landfills.")



#returns the array


def displayALternativesAndInfo():
    return popularProducts

#returns the information to do with each array item


def returnArray(Item):
    if (Item == "Water Bottle"):
        return popularProducts[0]
    elif (Item == "Toilet Paper"):
        return popularProducts[1]
    elif (Item == "Clothing"):
        return popularProducts[2]
    elif (Item == "Single Use Plastic Packaging"):
        return popularProducts[3]
    elif (Item == "Single Use Cleaning Products"):
        return popularProducts[4]
    elif (Item == "New Things"):
        return popularProducts[5]
    elif (Item == "Food"):
        return popularProducts[6]
    elif (Item == "Tea"):
        return popularProducts[7]


#when program is running
if __name__ == "__main__":

    print(displayALternativesAndInfo())
    print(returnArray("tea"))
