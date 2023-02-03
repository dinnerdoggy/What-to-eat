#Check the READ ME in the git for a full explanation of this program
import pickle

#Loading the "ingredients" dictionary
with open("ingredients.pickle", "rb") as f:
    g = pickle.load(f)

#Setting up functions that can search for possible recipes
eggs = g.get("eggs")
bacon = g.get("bacon slices")
bread = g.get("bread")
lettuce = g.get("lettuce")
tomato = g.get("tomato")
mayonaise = g.get("mayonaise")
butter = g.get("butter")

def breakfast():
    if eggs >= 3 and bacon >= 3 and butter >= 1:
        print("eggs and bacon")
    else:
        pass

def BLT():
    if bread >= 2 and bacon >= 2 and lettuce >= 1 and tomato >= 1 and mayonaise >= 1:
        print("BLT")
    else:
        pass

#Adding new groceries to the dictionary by user input.
#The amounts are based off of serving sizes per unit.
# - 12 eggs in a carton, 30 servings in a jar of mayo etc.
print("")
print("What new groceries did you bring home? When finished adding ingredients, type, 'done' If no new groceries, type 'nothing'")
print("")
print(g)
while True:
    groceries = input()

    if groceries == "eggs":
        g['eggs'] += 12
    elif groceries == "bacon":
        g['bacon slices'] += 19
    elif groceries == "bread":
        g['bread'] += 20
    elif groceries == "lettuce":
        g['lettuce'] += 30
    elif groceries == "tomato":
        g['tomato'] += 5
    elif groceries == "mayonaise":
        g['mayonaise'] += 30
    elif groceries == "butter":
        g['butter'] += 8
    elif groceries == "nothing":
        print("Nothing new? Okay :)")
        print("")
        break
    elif groceries == "done":
        break
    else:
        g[groceries] = 0
        print("How many serving are in", groceries, "?")
        servings = input()
        g[groceries] = servings

#List updated list of ingredients
print("Here is your updated list of in-house ingredients")
print(g)

#Print list of recipes possible from ingredients present
print("")
print("You can make the following:")
print("")

breakfast()
BLT()

print("")

#User inputs chosen recipe
print("What will you make? If nothing, type 'nothing'")

choice = input()

#Print user chosen Recipe and subtract corresponding ingredients from
#the g dictionary
print("")
if choice == "BLT":
    g['lettuce'] -= 1
    g['bacon slices'] -= 2
    g['tomato'] -= 1
    g['bread'] -= 2
    g['mayonaise'] -= 1
    fh = open("BLT_recipe.txt")
    for line in fh:
        print(line)
elif choice == "eggs and bacon":
    g['eggs'] -= 3
    g['bacon slices'] -= 3
    fh = open("Eggs & Bacon recipe.txt")
    for line in fh:
        print(line)
elif choice == "nothing":
    print("Thanks! See ya later!")
else:
    print("***Invalid input. Please type the dish exactly as it's listed.")

# Save the dictionary to a file
with open("ingredients.pickle", "wb") as f:
    pickle.dump(g, f)
