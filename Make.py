#OUTLINE**************
#Add ingredients
#Search for possible recipes
#Print list of recipes possible from ingredients present
#User inputs chosen recipe
#Print user chosen Recipe

#Adding ingredients
g = {}
g.update({"eggs": 10})
g.update({"bacon slices": 19})
g.update({"bread": 20})
g.update({"lettuce": 5})
g.update({"tomato": 2})
g.update({"mayonaise": 30})

#Search for possible recipes
eggs = g.get("eggs")
bacon = g.get("bacon slices")
bread = g.get("bread")
lettuce = g.get("lettuce")
tomato = g.get("tomato")
mayo = g.get("mayonaise")

def breakfast():
    if eggs >= 3 and bacon >= 3:
        print("You can make eggs and bacon!")
    else:
        pass

def BLT():
    if bread >= 2 and bacon >= 2 and lettuce >= 1 and tomato >= 1 and mayo >= 1:
        print("You can make a BLT!")
    else:
        pass

breakfast()
BLT()


#Print list of recipes possible from ingredients present


#User inputs chosen recipe


#Print user chosen Recipe



#Printing the recipe
#fh = open("Eggs and Bacon.txt")
#count = 0
#for x in fh :
    #print(x)
