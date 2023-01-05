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

#Search for possible recipes
eggs = g.get("eggs")
bacon = g.get("bacon slices")

def breakfast():
    if eggs >= 3 and bacon >= 3:
        print("You can make eggs and bacon!")
    else:
        print("You need to get groceries")

breakfast()


#Print list of recipes possible from ingredients present


#User inputs chosen recipe


#Print user chosen Recipe



#Printing the recipe
#fh = open("Eggs and Bacon.txt")
#count = 0
#for x in fh :
    #print(x)
