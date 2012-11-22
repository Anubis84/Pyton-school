'''
Created on 13/11/2012

@author: Anubis
'''
#Dette er opgave 1 på side 69 i bogen
if 0:
    print("true")
else:
    print("false")

if 1:
    print("true")
else:
    print("false")

if 2:
    print("true")
else:
    print("false")

if 3:
    print("true")
else:
    print("false")

if 4:
    print("true")
else:
    print("false")

#Dette er opgfave nr 2 på side 69 i bogen
#x = int(input("enter number"))
#if ( x< 9) and (x >0):
#   print(x)

#Dette er opgave 3 på side 69 i bogen

Mylist = ["top", "ned", "top"]
if "op" == Mylist[0]:
    print("is here")

elif "ned" == Mylist[1]:
    print(Mylist[1])

else:
    print("they are not here")

# Dette er opgave 4 på side 69 i bogen

fridge = {"milk":"let milk","chees":"blue chees", "butter":"rocksaltbutter"}

food_sought = "butter"

for foodkeys in fridge:
    print("\n looking at: %s"% foodkeys)
    if foodkeys == food_sought:
        print("key: %s \tValue: %s"%(foodkeys, fridge[food_sought] ))
        break
    else:
        print("it was not in the list")
        
#Dette er opgave 5 på side 69 i bogen

fridge_list = []

for foodkeys in fridge:
    fridge_list.append(foodkeys)
    print( fridge_list)
    
while fridge_list:
    if fridge_list.pop()== food_sought:   
        print( "Its there again ")
        break
else:
    print("not found")


#Dette er opgave 5 i bogen på side 69

try:
    wrongkeys = fridge ["gote meat"]
except KeyError:
    print("This is not in the fridge")

try:
    goodkeys = fridge["milk"]
    print(goodkeys)
except KeyError:
    print("This is in the fridge")
    
