#Global Variables time

'''
Maybe we can make a map? maybe something like this:
|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 6 | 7 | 8 | 9 | 10|
|---|---|---|---|---|
| 11| 12| 13| 14| 15|
|---|---|---|---|---|
| 16| 17| 18| 19| 20|
|---|---|---|---|---|
| 21| 22| 23| 24| 25|
|---|---|---|---|---|
'''

locationDescription = {1:"You come to a lake. There is an island in the middle of the lake.",
                        2:"You are at a crossroad.",
                        3:"Fall into a hole.\n Game Over."}

lookDescription =     {1:"You see a lake in the distance",
                        2:"You see a fork in the road in the distance",
                        3:"You see a chasm in the distance"}

def main(): #Let's throw everything into a function. Makes things easier later. The less "Global" stuff we have the better.
  print('''
  *******************************************************************************
            |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/_____ /
  *******************************************************************************
  ''')
  print("Welcome to Treasure Island. ")
  print("Your mission is to find the treasure. ") 

  direction = input('You are at a crossroad. Where do you want to go? Type "Left" or "Right".').lower()
  if  direction== "left":
    swim = input('You come to a lake. There is an island in the middle of the lake. \n Type "Wait" to wait for a boat. Type "Swim" to swim across\n').lower()
    if swim == "wait":
      door = input("You arrive at the island unharmed. There is a house with three doors.\n  one Red, one Yellow and one Blue. Which colour do you choose? \n").lower()
      if door == "yellow":
        print("You Win!")
      elif door == "red":
        print("Burned by fire. \n Game Over.")
      elif door == "blue":
        print("Eaten by beats. \n Game Over.") 
      else:
        print("Game Over.")
    else:
      print("Attacked by trout.\n Game Over.")
  else:
    print("Fall into a hole.\n Game Over.")

def look(currentLocation, direction): # we can use something like this to start generalizing new features. 
      #To implement this feature we need to keep track of our current location on the board, then if the direction they move to is valid we can then move them and display the relevant locationDescription
      if isValidDirection():
            lookDescription = lookDescription[1]
      lookDescription = "You try your best to look in that direction. But alas, you cannot (try another direction)"
      return(lookDescription)

def movement(currentLocation, direction):
      #To implement this feature we need to keep track of our current location on the board, then if the direction they move to is valid we can then move them and display the relevant lookDescription
      if isValidDirection():    
        locationDescription = locationDescription[1]
      else:
            locationDescription = "You would love to move there but unfortunatly that is not possible (try another direction)"
      return(locationDescription)

def isValidDirection(currentLocation, direction):
      #how can we tell if the direction is off the board?
      return(True)
main() #start the main function
