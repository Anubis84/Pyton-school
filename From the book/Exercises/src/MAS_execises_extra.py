'''
Created on 09/11/2012

@author: Anubis
'''

def makeSandWich(sandwichParts):
    if ("Bread" in sandwichParts) and \
    ("Butter" in sandwichParts) and\
    ("Jam" in sandwichParts):
        return "Delicious Sandwich"
    else:
        return "Unable to make sandwich"


def GoBuyFood(missingFood):
    return missingFood


def CheckFood(availableFood):
    missingFood = []
    for ingredient in ["Bread", "Butter", "Jam"]:
        if ingredient not in availableFood:
            missingFood.append(ingredient)
    return missingFood


def MAS(availableFood):
    missingFood = CheckFood(availableFood)
    print("We do not have:", missingFood)
    foodBought = GoBuyFood(missingFood)
    print("We have bought:", foodBought)
    print(makeSandWich(availableFood + foodBought))


def checkStore(storeInventory):
    if ("Bread" in storeInventory) and \
    ("Butter" in storeInventory) and\
    ("Jam" in storeInventory):
        return "The store has the food we need for a sandwich"
    else:
        return "the store has run out of the food we need to make a sandwich"
    
    
Food = []
storeInventory = ["Bread", "Butter", "Jam"]
MAS(Food)
