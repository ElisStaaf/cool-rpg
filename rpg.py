#!/bin/python3

"""
RPG Game
========

A pretty cool rpg game! It does things... That
an RPG would do. Like... It works..? Eh, it's a
functional project, and that's all that matters!

python :: >= 3.0
authors :: { Eyv-cyber, ElisStaaf }
license :: {
    This code is completely released onto the public
    domain, which means that the authors of this project
    seize the rights to prevent you, or anybody else, from
    using/modifying this source code. This code is for the
    people, not for the authors. This code is not licensed.
}
"""

import sys
import os
import signal
import time
import threading

# Raise an error if user is running an
# outdated version of python.
if sys.version_info <= (3, 0):
    print("[ERROR]: This python script was made for python 3.0 or higher.")
    exit(1)

def signal_handler(signal, frame):
    print("")
    exit(0)

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def showInstructions():
  # print a main menu and the commands
  print("""
RPG Game
========
Commands:
  go [direction]
  get [item]
========
Get to the garden a
key and a potion.
Avoid the monsters!
""")

def showStatus():
  # print the player's current status
  print("---------------------------")
  print("You are in the " + currentRoom)
  # print the current inventory
  print("Inventory : " + str(inventory).replace("'", "\"").replace("[", "{").replace("]", "}"))
  # print an item if there is one
  if "item" in rooms[currentRoom]:
    print("You see a " + rooms[currentRoom]["item"])
  print("---------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {   
    "Hall" : { 
        "south" : "Kitchen",
        "east" : "Dining Room",
        "item" : "key",
    },
    "Kitchen" : {
        "north" : "Hall",
        "item" : "monster"
    },
    "Dining Room" : {
        "west" : "Hall",
        "south" : "Garden"
    },
    "Garden" : {
        "north" : "Dining Room",
        "item" : "potion"
    }
}

# start the player in the Hall
currentRoom = "Hall"

clear()
showInstructions()

# loop forever
while True:
  signal.signal(signal.SIGINT, signal_handler)
  showStatus()
  # get the player's next "move"
  # .split() breaks it up into a list array
  # e.g typing "go east" would give the list:
  # ["go","east"]
  move = ""
  while move == "":  
    move = input(">")

  move = move.lower().split()

  # if they type "go" first
  if move[0] == "go":
    # check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      # set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    # there is no door (link) to the new room
    else:
        print("You can\'t go that way!")

  # if they type "get" first
  if move[0] == "get" :
    # if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
      # add the item to their inventory
      inventory += [move[1]]
      # display a helpful message
      print(move[1] + " got!")
      # delete the item from the room
      del rooms[currentRoom]["item"]
    # otherwise, if the item isn"t there to get
    else:
      # tell them they can't get it
      print("Can\'t get " + move[1] + "!")
# player loses if they enter a room with a monster
  if "item" in rooms[currentRoom] and "monster" in rooms[currentRoom]["item"]:
    print("A monster has got you ... GAME OVER!")
    break
  # player wins if they get to the garden with a key and a potion
  if currentRoom == "Garden" and "key" in inventory and "potion" in inventory:
    print("You escaped the house ... YOU WON!")
    break
