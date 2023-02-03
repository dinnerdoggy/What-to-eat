Make is a prototype that still needs work to be more user-friendly.
The idea behing the program is that it can give you a list of all the recipes
you can possibly make, based on the ingredients you actually have at home.
Right now it only has two recipes for prototyping purposes, but this can be expanded infinitely.

When the program opens, it will ask you what new ingredients you have, so If you just went shopping
you would enter in what you have. It will then store those into the pickle file to keep track of your 
food. 

If you didn't buy any groceries, and you're just looking for something to cook, you can skip this part 
and it will then show you a list of recipes that you can make with what you have. Once you select
your chosen recipe, it will print out the recipe for you to follow along, as well as subtract the 
used ingredients from the dictionary.

To do:
------
*The "else clause" in lines 59 - 63 work, but are problematic in their current form. If there is a user error, there currently
 is no way to undo the error for the user, and so whatever mistake is made will become recorded into the dictionary.

Things that would make this app consumer friendly:
--------------------------------------------------
*A gui with button input rather than typing that can help eliminate user error.

*Smart fridge integration for less user input overall

*barcode or receipt scanning for grocery input

*any amount of automation to reduce user input

****Run the program in your chosen shell. You have to have all the files in the same folder for the program to work****
