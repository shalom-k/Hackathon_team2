popularProducts = [[]]

#create a 2d array to store the information for reduce

popularProducts[0].append("Water Bottle")
popularProducts[0].append("Instead buying one use plastic bottle buy a reusable water bottle if\n you are opposed to " +
                          "tap water buy a large bottle of water,\n or a water filteration\n system you can use to refill bottle")
popularProducts[0].append("doing this can reduce up to 156 bottles per year.")



popularProducts.append([])
popularProducts[1].append("Toilet Paper")
popularProducts[1].append(
    "Instead of using toilet papers from trees use bamboo toilet paper such as\n bumboo or even better use a bidet to totally\n reduce this source of paper watse")
popularProducts[1].append("3.7 gallons of water a day can be saved using a bidet.\n Bamboo is the fastest growing plant and only takes\n 3-5 years to mature while tre" +
                          "es can take\n 25-40 years to replace. It also supports rural development\n and giving farmers a sustainable income.")

popularProducts.append([])
popularProducts[2].append("Clothing")
popularProducts[2].append("Buy second hand items")
popularProducts[2].append("Limits CO2 emissions, the use of pesticides and fertilizers,\n and billions of liters of water that would have been\n needed to generate new clothes." +
                          "Less cloths would\n need to be sent to landfills")

popularProducts.append([])
popularProducts[3].append("single use plastic packaging")
popularProducts[3].append("Visit stores which encourage you to refill\n your own glass containers instead of buying new plastic\n packaging each time." +
                          "You can also\n consider buying items in bulk.")
popularProducts[3].append("reduces the number of plastic waste produced")

popularProducts.append([])
popularProducts[4].append("single use cleaning products")
popularProducts[4].append("instead of buying single use cleaning products the throwing\n out the plastic bottle " +
                          "buy cleaning tablets\n which you just add water and resuse a glass container\n to store the cleaning products. An example is Blueland")
popularProducts[4].append("reduces the number of plastic waste produced")

popularProducts.append([])
popularProducts[5].append("New things")
popularProducts[5].append(
    "Instead of buying new things consider the items\n you already own in your home. Think of whether you\n really need that item.")
popularProducts[5].append(
    "Reduces the energy used to build those items \nand Co2 to ship them, ensures old items dont go to waste")

popularProducts.append([])
popularProducts[6].append("food")
popularProducts[6].append(
    "compost your own food watse and use it as a fertilizer")
popularProducts[6].append(
    "reduces food waste sent to a landfill, ensures food waste is properly used")

popularProducts.append([])
popularProducts[7].append("tea")
popularProducts[7].append("drink loose leaf tea")
popularProducts[7].append(
    "Plastic accounts for roughly 25% of the teabag. By switching to\n loose leaf you will reduce the amount of plastic ending up in landfills")

#popularProducts.append([])
#popularProducts[8].append("")
#popularProducts[8].append("")
#popularProducts[8].append("")

#popularProducts.append([])
#popularProducts[9].append("")
#popularProducts[9].append("")
#popularProducts[9].append("")

#returns the array

def displayALternativesAndInfo():
    return popularProducts

#returns the information to do with each array item
def returnArray(Item):
    if (Item == "water bottle"):
        return popularProducts[0]
    elif (Item == "Toilet paper"):
        return popularProducts[1]
    elif (Item == "Clothing"):
        return popularProducts[2]
    elif (Item == "single use plastic packaging"):
        return popularProducts[3]
    elif (Item == "single use cleaning products"):
        return popularProducts[4]
    elif (Item == "New things"):
        return popularProducts[5]
    elif (Item == "food"):
        return popularProducts[6]
    elif (Item == "tea"):
        return popularProducts[7]

#when program is running
if __name__ == "__main__":

    print(displayALternativesAndInfo())
    print(returnArray("tea"))
