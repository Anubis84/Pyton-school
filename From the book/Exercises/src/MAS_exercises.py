'''
Created on 09/11/2012

@author: Anubis
'''
def Bbread():
    return "bread"

def Bbutter():
    return "Butter"

def Jam():
    return "Jam"

def Slap():
    return "Sandwich"

Listsandwich = ("Bread","Butter","Jam","Sandwich")

Food = []
Food.append(Bbread())
Food.append(Bbutter())
Food.append(Jam())
Food.append(Slap())

print("I went to the store to get %s and %s and %s to make a %s"%Listsandwich  )
