popularProducts = [[]]

#tap water and water bottle, if opposed to tap buy a big bottle of bottled water and refill water bottle
#this will reduce up to 156 plastic bottles per year
popularProducts[0].append("water bottle")
popularProducts[0].append("instead buying one use plastic bottle buy a reusable water bottle if you are opposed to " +
                          "tap water buy a large bottle of water, or a water filteration system you can use to refill bottle")
popularProducts[0].append("doing this can reduce up to 156 bottles per year")    


#bumboo toilet paper made of bamboo
#the fastest growing plant on the planet! And it’s technically a grass, so with responsible farming, after an initial 3-5 year period
#to reach maturity, it can be re-harvested year after year, for as many as 40 -70 years! Compare this to trees that typically take
#25-40 years to mature and once harvested don't always re-grow naturally and a new tree must be planted.
#in China, most of the bamboo is grown by rural smallholders and administrated through co-operatives, thus supporting rural development and giving farmers a sustainable income.
popularProducts.append([])
popularProducts[1].append("Toilet paper")
popularProducts[1].append("Instead of using toilet papers from trees use bamboo toilet paper such as bumboo or even better use a bidet to totally reduce this source of paper watse")
popularProducts[1].append("3.7 gallons of water a day can be saved using a bidet. bamboo is the fastest growing plant and only takes 3-5 years to mature while tre" +
                          "es can take 25-40 years to replace. it also supports rural development and giving farmers a sustainable income")  

popularProducts.append([])
popularProducts[2].append("Clothing")
popularProducts[2].append("Buy second hand items")
popularProducts[2].append("Limits CO2 emissions, the use of pesticides and fertilizers, and billions of liters of water that would have been needed to generate new clothes." +
                          "Less cloths would need to be sent to landfills")

popularProducts.append([])
popularProducts[3].append("single use plastic packaging")
popularProducts[3].append("Visit stores which encourage you to refill your own glass containers instead of buying new plastic packaging each time." +
                          "You can also consider buying items in bulk.")
popularProducts[3].append("reduces the number of plastic waste produced")

popularProducts.append([])
popularProducts[4].append("single use cleaning products")
popularProducts[4].append("instead of buying single use cleaning products the throwing out the plastic bottle "+
                          "buy cleaning tablets which you just add water and resuse a glass container to store the cleaning products. An example is Blueland")
popularProducts[4].append("reduces the number of plastic waste produced")

popularProducts.append([])
popularProducts[5].append("New things")
popularProducts[5].append("Instead of buying new things consider the items you already own in your home. Think of whether you really need that item.")
popularProducts[5].append("Reduces the energy used to build those items and Co2 to ship them, ensures old items dont go to waste")

popularProducts.append([])
popularProducts[6].append("food")
popularProducts[6].append("compost your own food watse and use it as a fertilizer")
popularProducts[6].append("reduces food waste sent to a landfill, ensures food waste is properly used")

popularProducts.append([])
popularProducts[7].append("tea")
popularProducts[7].append("drink loose leaf tea")
popularProducts[7].append("Plastic accounts for roughly 25% of the teabag. By switching to loose leaf you will reduce the amount of plastic ending up in landfills")

popularProducts.append([])
popularProducts[8].append("")
popularProducts[8].append("")
popularProducts[8].append("")

popularProducts.append([])
popularProducts[9].append("")
popularProducts[9].append("")
popularProducts[9].append("")


def displayALternativesAndInfo():
    return popularProducts

def returnArray(Item):
    if (Item == "water bottle"):
        return popular[0]
    else if (Item == "Toilet paper"):
        return popular[1]
    else if (Item == "Clothing"):
        return popular[2]
    else if (Item == "single use plastic packaging"):
        return popular[3]
    else if (Item == "single use cleaning products"):
        return popular[4]
    else if (Item == "New things"):
        return popular[5]
    else if (Item == "food"):
        return popular[6]
    else if (Item == "tea"):
        return popular[7]

if __name__ == "__main__":
    
    print(displayALternativesAndInfo())
