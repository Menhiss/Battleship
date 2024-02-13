#NAME: Michael Dunne
#DATE: May 26, 2023
#This is my final project

import os
import sys
import random
import time
from colorama import Fore, Back, Style
from getkey import getkey, keys

#converts letter to a corresponding number on grid
def letter2Num(letter):
  if letter == "a" or letter == "A":
    return 1
  elif letter == "b" or letter == "B":
    return 2
  elif letter == "c" or letter == "C":
    return 3
  elif letter == "d" or letter == "D":
    return 4
  elif letter == "e" or letter == "E":
    return 5
  elif letter == "f" or letter == "F":
    return 6
  elif letter == "g" or letter == "G":
    return 7
  elif letter == "h" or letter == "H":
    return 8
  elif letter == "i" or letter == "I":
    return 9
  elif letter == "j" or letter == "J":
    return 10
  else:
    return False
    
#creates a blank grid
def gridInitialize():
  
  grid = []
  #makes a grid that is one too big
  for i in range(11):
    grid.append(["🟦"]*11)

  #changes top and left row to be numbers and letters
  grid[0][0] = Fore.BLUE +  "   "
  grid[0][1] = "A "
  grid[0][2] = "B "
  grid[0][3] = "C "
  grid[0][4] = "D "
  grid[0][5] = "E "
  grid[0][6] = "F "
  grid[0][7] = "G "
  grid[0][8] = "H "
  grid[0][9] = "I "
  grid[0][10] = "J "
  grid[1][0] = " 1"
  grid[2][0] = " 2"
  grid[3][0] = " 3"
  grid[4][0] = " 4"
  grid[5][0] = " 5"
  grid[6][0] = " 6"
  grid[7][0] = " 7"
  grid[8][0] = " 8"
  grid[9][0] = " 9"
  grid[10][0] = "10"
  
  return grid

#prints the chosen grid ina nice format
def gridPrint(grid):
  for i in grid:
    gridDisplay = ''.join(i)
    print(gridDisplay)

#places the chosen boat on the grid
def placeBoats(boat, grid):
  boatSquares = []
  #sets variables
  rotated = False
  count = 0
  verticalCount = 1
  moveDown = False
  #this loop will run until the boat has been spawned
  while True:
    #increases the count of where to place the boat
    count += 1
    #if it moves too far right it sets movedown to true because there is no space left to spawn the boat in the top left and then resets the count
    if count > 10:
      moveDown = True
      count = 1
    #if the top row is full it increases the vertical count to let it move down
    if moveDown == True:
      verticalCount += 1
    #in this try and except it attempts to place the boat
    try:
      #checks if the squares where the boat should go are water
      for i in range(boat):
        if grid[i+verticalCount][count] != "🟦":
          raise ValueError
      #since the squares are safe it places the boat and exits 
      for i in range(boat):
        grid[i+verticalCount][count] = "⬛"
        boatSquares.append([i+verticalCount, count])
      break
    #if it doesn't pass the test it returns to the top of the loop
    except ValueError:
      continue
  #this loop will run until the boat is placed
  while True:
    os.system("clear")
    gridPrint(grid)
    print("\nW to move up\nA to move left\nS to move down\nD to move right\nR to rotate\nC to confirm")
    key = getkey()
    #this is if the user tries to move the boat up
    if key == "w" or key == "W":
      try:
        newBoatSquares = []
        #if it is in the top row it can't go up
        for i in boatSquares:
          if i[0] == 1:
            raise ValueError
        #if it is not rotated it only needs to look at top square and see if it is a boat
        if rotated == False:
          for i in boatSquares:
            if grid[i[0]-1][i[1]] == "⬛":
              raise ValueError
            break
        #it is rotated so it checks every square and sees if it is a boat
        else:
          for i in boatSquares:
            if grid[i[0]-1][i[1]] == "⬛":
              raise ValueError
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
          grid[i[0]-1][i[1]] = "⬛"
          newBoatSquares.append([i[0]-1, i[1]])
        boatSquares = newBoatSquares
      #if it didn't pass a check it tells the user
      except ValueError:
        print(Fore.RED + "The boat can't move that way")
        time.sleep(1)
    #this is if the user tries to move the boat left
    elif key == "a" or key == "A":
      try:
        newBoatSquares = []
        #if it is in the left column it can't go left
        for i in boatSquares:
          if i[1] == 1:
            raise ValueError
        #if it is not rotated so it checks every square and sees if it is a boat
        if rotated == False:
          for i in boatSquares:
            if grid[i[0]][i[1]-1] == "⬛":
              raise ValueError
        #it is rotated so it only needs to look at left square and see if it is a boat
        else:
          for i in boatSquares:
            if grid[i[0]][i[1]-1] == "⬛":
              raise ValueError
            break
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
          grid[i[0]][i[1]-1] = "⬛"
          newBoatSquares.append([i[0], i[1]-1])
          boatSquares = newBoatSquares
          #if it didn't pass a check it tells user
      except ValueError:
        print(Fore.RED + "The boat can't move that way")
        time.sleep(1)
    #this is if the user tries to move the boat down
    elif key == "s" or key == "S":
      try:
        newBoatSquares = []
        #if it is in the bottom row it can't go down
        if boatSquares[len(boatSquares)-1][0] == 10:
          raise ValueError
        #if it is not rotated it only needs to look at bottom square and see if it is a boat
        if rotated == False:
          if grid[boatSquares[len(boatSquares)-1][0]+1][boatSquares[len(boatSquares)-1][1]] == "⬛":
            raise ValueError
        #it is rotated so it checks every square and sees if it is a boat
        else:
          for i in boatSquares:
            if grid[i[0]+1][i[1]] == "⬛":
              raise ValueError
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
        for i in boatSquares:
          grid[i[0]+1][i[1]] = "⬛"
          newBoatSquares.append([i[0]+1, i[1]])
          boatSquares = newBoatSquares
      #if it didn't pass a check it tells the user
      except ValueError:
        print(Fore.RED + "The boat can't move that way")
        time.sleep(1)
    #this is if the user tries to move the boat right
    elif key == "d" or key == "D":
      try:
        newBoatSquares = []
        #if it is in the right column it can't go right
        if boatSquares[len(boatSquares)-1][1] == 10:
          raise ValueError
        #if it is not rotated so it checks every square and sees if it is a boat
        if rotated == False:
          for i in boatSquares:
            if grid[i[0]][i[1]+1] == "⬛":
              raise ValueError
        #it is rotated so it only needs to look at right square and see if it is a boat
        else:
          if grid[boatSquares[len(boatSquares)-1][0]][boatSquares[len(boatSquares)-1][1]+1] == "⬛":
            raise ValueError
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
        for i in boatSquares:
          grid[i[0]][i[1]+1] = "⬛"
          newBoatSquares.append([i[0], i[1]+1])
          boatSquares = newBoatSquares
      #if it didn't pass a check it tells the user
      except ValueError:
        print(Fore.RED + "The boat can't move that way")
        time.sleep(1)
    #this is for when the user is ready to place the boat
    elif key == "c" or key == "C":
      return boatSquares
    #this is if the user tries to rotate the boat
    elif key == "r" or key == "R":
      newBoatSquares = []
      try:
        for i in boatSquares:
          #it first sees if a new square is a boat
          if grid[i[1]][i[0]] == "⬛":
            #then it reverses the failing coordinate and sees if it is a part of the boat being rotated
            iReverse = i[::-1]
            if iReverse not in boatSquares:
              raise ValueError
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
          grid[i[1]][i[0]] = "⬛"
          newBoatSquares.append([i[1], i[0]])
          boatSquares = newBoatSquares
        #swaps rotated boolean
        if rotated == False:
          rotated = True
        else:
          rotated = False
      #if it didn't pass a check it tells the user
      except ValueError:
        print(Fore.RED + "The boat can't move that way")
        time.sleep(1)

#places boat for computer
def computerPlaceBoats(boat, grid):
  boatSquares = []
  #sets variables
  rotated = False
  count = 0
  verticalCount = 1
  moveDown = False
  #this loop will run until the boat has been spawned
  while True:
    #increases the count of where to place the boat
    count += 1
    #if it moves too far right it sets movedown to true because there is no space left to spawn the boat in the top left and then resets the count
    if count > 10:
      moveDown = True
      count = 1
    #if the top row is full it increases the vertical count to let it move down
    if moveDown == True:
      verticalCount += 1
    #in this try and except it attempts to place the boat
    try:
      #checks if the squares where the boat should go are water
      for i in range(boat):
        if grid[i+verticalCount][count] != "🟦":
          raise ValueError
      #since the squares are safe it places the boat and exits 
      for i in range(boat):
        grid[i+verticalCount][count] = "⬛"
        boatSquares.append([i+verticalCount, count])
      break
    #if it doesn't pass the test it returns to the top of the loop
    except ValueError:
      continue
  #generates random key instead of user inputting it 300 times
  for i in range(300):
    key = random.choice(["w", "a", "s", "d", "r"])
    #this is if the user tries to move the boat up
    if key == "w" or key == "W":
      try:
        newBoatSquares = []
        #if it is in the top row it can't go up
        for i in boatSquares:
          if i[0] == 1:
            raise ValueError
        #if it is not rotated it only needs to look at top square and see if it is a boat
        if rotated == False:
          for i in boatSquares:
            if grid[i[0]-1][i[1]] == "⬛":
              raise ValueError
            break
        #it is rotated so it checks every square and sees if it is a boat
        else:
          for i in boatSquares:
            if grid[i[0]-1][i[1]] == "⬛":
              raise ValueError
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
          grid[i[0]-1][i[1]] = "⬛"
          newBoatSquares.append([i[0]-1, i[1]])
        boatSquares = newBoatSquares
      #if it didn't pass a check it tells the user
      except ValueError:
        pass
    #this is if the user tries to move the boat left
    elif key == "a" or key == "A":
      try:
        newBoatSquares = []
        #if it is in the left column it can't go left
        for i in boatSquares:
          if i[1] == 1:
            raise ValueError
        #if it is not rotated so it checks every square and sees if it is a boat
        if rotated == False:
          for i in boatSquares:
            if grid[i[0]][i[1]-1] == "⬛":
              raise ValueError
        #it is rotated so it only needs to look at left square and see if it is a boat
        else:
          for i in boatSquares:
            if grid[i[0]][i[1]-1] == "⬛":
              raise ValueError
            break
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
          grid[i[0]][i[1]-1] = "⬛"
          newBoatSquares.append([i[0], i[1]-1])
          boatSquares = newBoatSquares
          #if it didn't pass a check it tells user
      except ValueError:
       pass
    #this is if the user tries to move the boat down
    elif key == "s" or key == "S":
      try:
        newBoatSquares = []
        #if it is in the bottom row it can't go down
        if boatSquares[len(boatSquares)-1][0] == 10:
          raise ValueError
        #if it is not rotated it only needs to look at bottom square and see if it is a boat
        if rotated == False:
          if grid[boatSquares[len(boatSquares)-1][0]+1][boatSquares[len(boatSquares)-1][1]] == "⬛":
            raise ValueError
        #it is rotated so it checks every square and sees if it is a boat
        else:
          for i in boatSquares:
            if grid[i[0]+1][i[1]] == "⬛":
              raise ValueError
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
        for i in boatSquares:
          grid[i[0]+1][i[1]] = "⬛"
          newBoatSquares.append([i[0]+1, i[1]])
          boatSquares = newBoatSquares
      #if it didn't pass a check it tells the user
      except ValueError:
        pass
    #this is if the user tries to move the boat right
    elif key == "d" or key == "D":
      try:
        newBoatSquares = []
        #if it is in the right column it can't go right
        if boatSquares[len(boatSquares)-1][1] == 10:
          raise ValueError
        #if it is not rotated so it checks every square and sees if it is a boat
        if rotated == False:
          for i in boatSquares:
            if grid[i[0]][i[1]+1] == "⬛":
              raise ValueError
        #it is rotated so it only needs to look at right square and see if it is a boat
        else:
          if grid[boatSquares[len(boatSquares)-1][0]][boatSquares[len(boatSquares)-1][1]+1] == "⬛":
            raise ValueError
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
        for i in boatSquares:
          grid[i[0]][i[1]+1] = "⬛"
          newBoatSquares.append([i[0], i[1]+1])
          boatSquares = newBoatSquares
      #if it didn't pass a check it tells the user
      except ValueError:
        pass
    #this is if the user tries to rotate the boat
    elif key == "r" or key == "R":
      newBoatSquares = []
      try:
        for i in boatSquares:
          #it first sees if a new square is a boat
          if grid[i[1]][i[0]] == "⬛":
            #then it reverses the failing coordinate and sees if it is a part of the boat being rotated
            iReverse = i[::-1]
            if iReverse not in boatSquares:
              raise ValueError
        #it has passed all checks and can make this movement so it makes the squares it was blue and the new squares white
        for i in boatSquares:
          grid[i[0]][i[1]] = "🟦"
          grid[i[1]][i[0]] = "⬛"
          newBoatSquares.append([i[1], i[0]])
          boatSquares = newBoatSquares
        #swaps rotated boolean
        if rotated == False:
          rotated = True
        else:
          rotated = False
      #if it didn't pass a check it tries again
      except ValueError:
        pass
  return boatSquares

#sets up grids for game
def setup():
  global playerOneGrid
  global playerOneHiddenGrid
  global playerTwoGrid
  global playerTwoHiddenGrid
  global playerOneDestroyer
  global playerOneSubmarine
  global playerOneCruiser
  global playerOneBattleship
  global playerOneCarrier
  global playerTwoDestroyer
  global playerTwoSubmarine
  global playerTwoCruiser
  global playerTwoBattleship
  global playerTwoCarrier
  global turn
  #makes the 4 grids
  playerOneGrid = gridInitialize()
  playerOneHiddenGrid = gridInitialize()
  playerTwoGrid = gridInitialize()
  playerTwoHiddenGrid = gridInitialize()
  #makes blank list for each ship
  playerOneDestroyer = []
  playerOneSubmarine = []
  playerOneCruiser = []
  playerOneBattleship = []
  playerOneCarrier = []
  playerTwoDestroyer = []
  playerTwoSubmarine = []
  playerTwoCruiser = []
  playerTwoBattleship = []
  playerTwoCarrier = []
  os.system("clear")
  #lets user choose between pvp and pve
  choice = input(Fore.WHITE + "What would you like to do?\n\t1. Player Vs. Player\n\t2. Player Vs. Computer\n")
  #2 player
  if choice == "1":
    #initializes booleans
    os.system("clear")
    destroyerUsed = False
    submarineUsed = False
    cruiserUsed = False
    battleshipUsed = False
    carrierUsed = False
    print(Fore.WHITE + "It is time for player one to place their boats")
    time.sleep(2)
    #loop that runs until all boats placed for player one
    while destroyerUsed == False or submarineUsed == False or cruiserUsed == False or battleshipUsed == False or carrierUsed == False:
      time.sleep(1)
      os.system("clear")
      print(Fore.WHITE +"Which boat would you like to place\n")
      if destroyerUsed == False:
        print(Fore.RED + "\t1. Destroyer\t⬛⬛")
      else:
        print(Fore.GREEN + "\t1. Destroyer\t⬛⬛")
      if submarineUsed == False:
        print(Fore.RED + "\t2. Submarine\t⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t2. Submarine\t⬛⬛⬛")
      if cruiserUsed == False:
        print(Fore.RED + "\t3. Cruiser\t\t⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t3. Cruiser\t\t⬛⬛⬛")
      if battleshipUsed == False:
        print(Fore.RED + "\t4. Battleship\t⬛⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t4. Battleship\t⬛⬛⬛⬛")
      if carrierUsed == False:
        print(Fore.RED + "\t5. Carrier\t\t⬛⬛⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t5. Carrier\t\t⬛⬛⬛⬛⬛")
      choice = input(Fore.WHITE + "\n")
      if choice == "1":
        if destroyerUsed == False:
          playerOneDestroyer = placeBoats(2, playerOneHiddenGrid)
          destroyerUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "2":
        if submarineUsed == False:
          playerOneSubmarine = placeBoats(3, playerOneHiddenGrid)
          submarineUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "3":
        if cruiserUsed == False:
          playerOneCruiser = placeBoats(3, playerOneHiddenGrid)
          cruiserUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "4":
        if battleshipUsed == False:
          playerOneBattleship = placeBoats(4, playerOneHiddenGrid)
          battleshipUsed = True
        else:
          playerOneBattleship = print(Fore.RED + "Already placed")
      elif choice == "5":
        if carrierUsed == False:
          playerOneCarrier = placeBoats(5, playerOneHiddenGrid)
          carrierUsed = True
        else:
          print(Fore.RED + "Already placed")
      else:
        print(Fore.RED + "Not valid")
    #initializes booleans
    destroyerUsed = False
    submarineUsed = False
    cruiserUsed = False
    battleshipUsed = False
    carrierUsed = False
    time.sleep(2)
    os.system("clear")
    time.sleep(1)
    print(Fore.WHITE + "It is time for player two to place their boats")
    time.sleep(1)
    #loop that runs until all boats placed for player two
    while destroyerUsed == False or submarineUsed == False or cruiserUsed == False or battleshipUsed == False or carrierUsed == False:
      time.sleep(2)
      os.system("clear")
      print(Fore.WHITE +"Which boat would you like to place\n")
      if destroyerUsed == False:
        print(Fore.RED + "\t1. Destroyer\t⬛⬛")
      else:
        print(Fore.GREEN + "\t1. Destroyer\t⬛⬛")
      if submarineUsed == False:
        print(Fore.RED + "\t2. Submarine\t⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t2. Submarine\t⬛⬛⬛")
      if cruiserUsed == False:
        print(Fore.RED + "\t3. Cruiser\t\t⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t3. Cruiser\t\t⬛⬛⬛")
      if battleshipUsed == False:
        print(Fore.RED + "\t4. Battleship\t⬛⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t4. Battleship\t⬛⬛⬛⬛")
      if carrierUsed == False:
        print(Fore.RED + "\t5. Carrier\t\t⬛⬛⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t5. Carrier\t\t⬛⬛⬛⬛⬛")
      choice = input(Fore.WHITE + "\n")
      if choice == "1":
        if destroyerUsed == False:
          playerTwoDestroyer = placeBoats(2, playerTwoHiddenGrid)
          destroyerUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "2":
        if submarineUsed == False:
          playerTwoSubmarine = placeBoats(3, playerTwoHiddenGrid)
          submarineUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "3":
        if cruiserUsed == False:
          playerTwoCruiser = placeBoats(3, playerTwoHiddenGrid)
          cruiserUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "4":
        if battleshipUsed == False:
          playerTwoBattleship = placeBoats(4, playerTwoHiddenGrid)
          battleshipUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "5":
        if carrierUsed == False:
          playerTwoCarrier = placeBoats(5, playerTwoHiddenGrid)
          carrierUsed = True
        else:
          print(Fore.RED + "Already placed")
      else:
        print(Fore.RED + "Not valid")
    os.system("clear")
    #randomly selects who goes first
    turn = random.randrange(1, 2)
    if turn % 2 == 0:
      print(Fore.WHITE + "Player one press anything to continue")
    else:
      print(Fore.WHITE + "Player two press anything to continue")
    key = getkey()
    game()
  #1 player
  elif choice == "2":
    #initializes booleans
    destroyerUsed = False
    submarineUsed = False
    cruiserUsed = False
    battleshipUsed = False
    carrierUsed = False
    #loop that runs until all boats placed for player one
    while destroyerUsed == False or submarineUsed == False or cruiserUsed == False or battleshipUsed == False or carrierUsed == False:
      time.sleep(1)
      os.system("clear")
      print(Fore.WHITE +"Which boat would you like to place\n")
      if destroyerUsed == False:
        print(Fore.RED + "\t1. Destroyer\t⬛⬛")
      else:
        print(Fore.GREEN + "\t1. Destroyer\t⬛⬛")
      if submarineUsed == False:
        print(Fore.RED + "\t2. Submarine\t⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t2. Submarine\t⬛⬛⬛")
      if cruiserUsed == False:
        print(Fore.RED + "\t3. Cruiser\t\t⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t3. Cruiser\t\t⬛⬛⬛")
      if battleshipUsed == False:
        print(Fore.RED + "\t4. Battleship\t⬛⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t4. Battleship\t⬛⬛⬛⬛")
      if carrierUsed == False:
        print(Fore.RED + "\t5. Carrier\t\t⬛⬛⬛⬛⬛")
      else:
        print(Fore.GREEN + "\t5. Carrier\t\t⬛⬛⬛⬛⬛")
      choice = input(Fore.WHITE + "\n")
      if choice == "1":
        if destroyerUsed == False:
          playerOneDestroyer = placeBoats(2, playerOneHiddenGrid)
          destroyerUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "2":
        if submarineUsed == False:
          playerOneSubmarine = placeBoats(3, playerOneHiddenGrid)
          submarineUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "3":
        if cruiserUsed == False:
          playerOneCruiser = placeBoats(3, playerOneHiddenGrid)
          cruiserUsed = True
        else:
          print(Fore.RED + "Already placed")
      elif choice == "4":
        if battleshipUsed == False:
          playerOneBattleship = placeBoats(4, playerOneHiddenGrid)
          battleshipUsed = True
        else:
          playerOneBattleship = print(Fore.RED + "Already placed")
      elif choice == "5":
        if carrierUsed == False:
          playerOneCarrier = placeBoats(5, playerOneHiddenGrid)
          carrierUsed = True
        else:
          print(Fore.RED + "Already placed")
      else:
        print(Fore.RED + "Not valid")
    #computer generates its grid
    playerTwoDestroyer = computerPlaceBoats(2, playerTwoHiddenGrid)
    playerTwoSubmarine = computerPlaceBoats(3, playerTwoHiddenGrid)
    playerTwoCruiser = computerPlaceBoats(3, playerTwoHiddenGrid)
    playerTwoBattleship = computerPlaceBoats(4, playerTwoHiddenGrid)
    playerTwoCarrier = computerPlaceBoats(5, playerTwoHiddenGrid)
    os.system("clear")
    print(Fore.WHITE + "Press anything to continue")
    key = getkey()
    computer()
  #not a valid option so it asks again
  else:
    print(Fore.RED + "Not valid")
    time.sleep(1)
    os.system("clear")
    setup()

#takes turns attacking against computer
def computer():
  global playerOneGrid
  global playerOneHiddenGrid
  global playerTwoGrid
  global playerTwoHiddenGrid
  global playerOneDestroyer
  global playerOneSubmarine
  global playerOneCruiser
  global playerOneBattleship
  global playerOneCarrier
  global playerTwoDestroyer
  global playerTwoSubmarine
  global playerTwoCruiser
  global playerTwoBattleship
  global playerTwoCarrier
  #initializes booleans
  playerOneDestroyerSunk = False
  playerOneSubmarineSunk = False
  playerOneCruiserSunk = False
  playerOneBattleshipSunk = False
  playerOneCarrierSunk = False
  playerTwoDestroyerSunk = False
  playerTwoSubmarineSunk = False
  playerTwoCruiserSunk = False
  playerTwoBattleshipSunk = False
  playerTwoCarrierSunk = False
  #sets up variables
  hit = False
  directions = [1, 2, 3, 4]
  breakCount = 0
  turn = 2
  while True:
    os.system("clear")
    #player 1
    if turn % 2 == 0:
      print(Fore.WHITE + "\t\tPlayer One\n\n")
      gridPrint(playerTwoGrid)
      print("\n\n")
      gridPrint(playerOneHiddenGrid)
      choice = input("\n\nWhere would you like to attack?\n\n").split()
      #validates the coordinate
      if len(choice) == 2 and choice[0].isalpha() and choice[1].isdigit():
        letter = letter2Num(choice[0])
        number = int(choice[1])
        if letter == False or number > 10 or number < 1:
          print("Not valid\n\nMake sure it is a point on the grid")
          time.sleep(0.5)
        #checks if it is a hit
        elif playerTwoHiddenGrid[number][letter] == "⬛":
          #reveals hit square
          playerTwoGrid[number][letter] = "🟥"
          playerTwoHiddenGrid[number][letter] = "🟥"
          #removes the hit square from whatever boat it is in
          if [number, letter] in playerTwoDestroyer:
            playerTwoDestroyer.remove([number, letter])
          elif [number, letter] in playerTwoSubmarine:
            playerTwoSubmarine.remove([number, letter])
          elif [number, letter] in playerTwoCruiser:
            playerTwoCruiser.remove([number, letter])
          elif [number, letter] in playerTwoBattleship:
            playerTwoBattleship.remove([number, letter])
          elif [number, letter] in playerTwoCarrier:
            playerTwoCarrier.remove([number, letter])
          print("That was a hit\n")
          time.sleep(1)
          #checks if any boats are sunk
          if playerTwoDestroyerSunk == False and playerTwoDestroyer == []:
            playerTwoDestroyerSunk = True
            print("You sunk the destroyer\n")
            time.sleep(1)
          if playerTwoSubmarineSunk == False and playerTwoSubmarine == []:
            playerTwoSubmarineSunk = True
            print("You sunk the submarine\n")
            time.sleep(1)
          if playerTwoCruiserSunk == False and playerTwoCruiser == []:
            playerTwoCruiserSunk = True
            print("You sunk the cruiser\n")
            time.sleep(1)
          if playerTwoBattleshipSunk == False and playerTwoBattleship == []:
            playerTwoBattleshipSunk = True
            print("You sunk the battleship\n")
            time.sleep(1)
          if playerTwoCarrierSunk == False and playerTwoCarrier == []:
            playerTwoCarrierSunk = True
            print("You sunk the carrier\n")
            time.sleep(1)
            #checks if all boats are sunk
          if playerTwoDestroyerSunk == True and playerTwoSubmarineSunk == True and playerTwoCruiserSunk == True and playerTwoBattleshipSunk == True and playerTwoCarrierSunk == True:
            print("You sunk all the ships\n")
            time.sleep(1)
            print("Player one wins")
            time.sleep(1)
            menu()
          print("You get to shoot again")
          time.sleep(1)
        #checks if water was attacked
        elif playerTwoHiddenGrid[number][letter] == "🟦":
          #reveals the missed square
          playerTwoGrid[number][letter] = "⬜"
          playerTwoHiddenGrid[number][letter] = "⬜"
          print("That was a miss")
          time.sleep(1)
          print("It is the computers turn")
          time.sleep(1)
          turn += 1
          os.system("clear")
        #not a hit or miss so it was already attacked
        else:
          print("You already attacked there")
          time.sleep(1)
      else:
        print("Not valid\n\nEnter like A 1") 
        time.sleep(2)
    #computer
    else:
      #checks to see if last attack was not a hit
      if hit == False:
        #generates where to attack
        squaresOver = 1
        r = random.randint(1, 10)
        c = random.randint(1, 10)
        #checks if it is a hit, reveals the square and makes the hit boolean true
        if playerOneHiddenGrid[r][c] == "⬛":
          playerOneHiddenGrid[r][c] = "🟥"
          hit = True
          #removes that square from whichever boat it was in
          if [r, c] in playerOneDestroyer:
            playerOneDestroyer.remove([r, c])
          elif [r, c] in playerOneSubmarine:
            playerOneSubmarine.remove([r, c])
          elif [r, c] in playerOneCruiser:
            playerOneCruiser.remove([r, c])
          elif [r, c] in playerOneBattleship:
            playerOneBattleship.remove([r, c])
          elif [r, c] in playerOneCarrier:
            playerOneCarrier.remove([r, c])
          #checks if any boats are sunk
          if playerOneDestroyerSunk == False and playerOneDestroyer == []:
            playerOneDestroyerSunk = True
            hit = False
            squaresOver = 1
            directions = [1, 2, 3, 4]
          if playerOneSubmarineSunk == False and playerOneSubmarine == []:
            playerOneSubmarineSunk = True
            hit = False
            squaresOver = 1
            directions = [1, 2, 3, 4]
          if playerOneCruiserSunk == False and playerOneCruiser == []:
            playerOneCruiserSunk = True
            hit = False
            squaresOver = 1
            directions = [1, 2, 3, 4]
          if playerTwoBattleshipSunk == False and playerOneBattleship == []:
            playerTwoBattleshipSunk = True
            hit = False
            squaresOver = 1
            directions = [1, 2, 3, 4]
          if playerOneCarrierSunk == False and playerOneCarrier == []:
            playerOneCarrierSunk = True
            hit = False
            squaresOver = 1
            directions = [1, 2, 3, 4]
        #if it is a miss it reveals it
        elif playerOneHiddenGrid[r][c] == "🟦":
          playerOneHiddenGrid[r][c] = "⬜"
          print("The computer's turn is over")
          turn += 1
        #it was already attack so the computer generates a new coordinate and tries again
        else:
          continue
      #this means that there is a boat currently trying to be sunk
      else:
        try:
          #the directions variable is defaulted to [1,2,3,4] but the directions often change
          #picks a random direction
          direction = random.choice(directions)
          #if it is up
          if direction == 1:
            #moves the attacked square up one and checks if it was a hit
            if playerOneHiddenGrid[r - squaresOver][c] == "⬛":
              playerOneHiddenGrid[r - squaresOver][c] = "🟥"
              #it was a hit so that direction is made the only option in directions
              directions = [direction]
              hit = True
              #removes it from its ship
              if [r - squaresOver, c] in playerOneDestroyer:
                playerOneDestroyer.remove([r - squaresOver, c])
              elif [r - squaresOver, c] in playerOneSubmarine:
                playerOneSubmarine.remove([r - squaresOver, c])
              elif [r - squaresOver, c] in playerOneCruiser:
                playerOneCruiser.remove([r - squaresOver, c])
              elif [r - squaresOver, c] in playerOneBattleship:
                playerOneBattleship.remove([r - squaresOver, c])
              elif [r - squaresOver, c] in playerOneCarrier:
                playerOneCarrier.remove([r - squaresOver, c])
              #checks if any boats were sunk
              if playerOneDestroyerSunk == False and playerOneDestroyer == []:
                playerOneDestroyerSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneSubmarineSunk == False and playerOneSubmarine == []:
                playerOneSubmarineSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneCruiserSunk == False and playerOneCruiser == []:
                playerOneCruiserSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneBattleshipSunk == False and playerOneBattleship == []:
                playerOneBattleshipSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneCarrierSunk == False and playerOneCarrier == []:
                playerOneCarrierSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
            #it was a miss so it reveals it
            elif playerOneHiddenGrid[r - squaresOver][c] == "🟦":
              playerOneHiddenGrid[r - squaresOver][c] = "⬜"
              print("The computer's turn is over")
              turn += 1
              #if there is only one direction and the ship didn't sink then it has to be the other way so it swaps the direction
              if len(directions) == 1:
                squaresOver = 1
                directions = [3]
              #it hasn't found the right direction so it just removes up from possible directions
              else:
                directions.remove(direction)
                squaresOver = 1
            #makes sure the square has been attacked
            elif playerOneHiddenGrid[r - squaresOver][c] == "🟥" or playerOneHiddenGrid[r - squaresOver][c] == "⬜":
              squaresOver += 1
              #breakCount allows me to exit from a while loop continue loop that breaks the code
              breakCount += 1
              if breakCount > 10:
                breakCount = 0
                hit = False
              continue
            #it isn't a square on the grid
            else:
              raise IndexError
          #if it is left
          elif direction == 2:
            #moves the attacked square left the amount of squaresOver it is supposed to be and checks if it was a hit
            if playerOneHiddenGrid[r][c - squaresOver] == "⬛":
              playerOneHiddenGrid[r][c - squaresOver] = "🟥"
              #it was a hit so that direction is made the only option in directions
              directions = [direction]
              hit = True
              #removes it from its ship
              if [r, c - squaresOver] in playerOneDestroyer:
                playerOneDestroyer.remove([r, c - squaresOver])
              elif [r, c - squaresOver] in playerOneSubmarine:
                playerOneSubmarine.remove([r, c - squaresOver])
              elif [r, c - squaresOver] in playerOneCruiser:
                playerOneCruiser.remove([r, c - squaresOver])
              elif [r, c - squaresOver] in playerOneBattleship:
                playerOneBattleship.remove([r, c - squaresOver])
              elif [r, c - squaresOver] in playerOneCarrier:
                playerOneCarrier.remove([r, c - squaresOver])
              #checks if any boats were sunk
              if playerOneDestroyerSunk == False and playerOneDestroyer == []:
                playerOneDestroyerSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
                directions = [1, 2, 3, 4]
              if playerOneSubmarineSunk == False and playerOneSubmarine == []:
                playerOneSubmarineSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneCruiserSunk == False and playerOneCruiser == []:
                playerOneCruiserSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneBattleshipSunk == False and playerOneBattleship == []:
                playerOneBattleshipSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneCarrierSunk == False and playerOneCarrier == []:
                playerOneCarrierSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
            #it was a miss so it reveals it
            elif playerOneHiddenGrid[r][c - squaresOver] == "🟦":
              playerOneHiddenGrid[r][c - squaresOver] = "⬜"
              print("The computer's turn is over")
              turn += 1
              #if there is only one direction and the ship didn't sink then it has to be the other way so it swaps the direction
              if len(directions) == 1:
                squaresOver = 1
                directions = [4]
              #it hasn't found the right direction so it just removes left from possible directions
              else:
                directions.remove(direction)
                squaresOver = 1
            #makes sure the square has been attacked
            elif playerOneHiddenGrid[r][c - squaresOver] == "🟥" or playerOneHiddenGrid[r][c - squaresOver] == "⬜":
              squaresOver += 1
              #breakCount allows me to exit from a while loop continue loop that breaks the code
              breakCount += 1
              if breakCount > 10:
                breakCount = 0
                hit = False
              continue
            #it isn't a square on the grid
            else:
              raise IndexError
          #if it is down
          elif direction == 3:
            #moves the attacked square down the amount of squaresOver it is supposed to be and checks if it was a hit
            if playerOneHiddenGrid[r + squaresOver][c] == "⬛":
              playerOneHiddenGrid[r + squaresOver][c] = "🟥"
              #it was a hit so that direction is made the only option in directions
              directions = [direction]
              hit = True
              #removes it from its ship
              if [r + squaresOver, c] in playerOneDestroyer:
                playerOneDestroyer.remove([r + squaresOver, c])
              elif [r + squaresOver, c] in playerOneSubmarine:
                playerOneSubmarine.remove([r + squaresOver, c])
              elif [r + squaresOver, c] in playerOneCruiser:
                playerOneCruiser.remove([r + squaresOver, c])
              elif [r + squaresOver, c] in playerOneBattleship:
                playerOneBattleship.remove([r + squaresOver, c])
              elif [r + squaresOver, c] in playerOneCarrier:
                playerOneCarrier.remove([r + squaresOver, c])
              #checks if an boats are sunk
              if playerOneDestroyerSunk == False and playerOneDestroyer == []:
                playerOneDestroyerSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneSubmarineSunk == False and playerOneSubmarine == []:
                playerOneSubmarineSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneCruiserSunk == False and playerOneCruiser == []:
                playerOneCruiserSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneBattleshipSunk == False and playerOneBattleship == []:
                playerOneBattleshipSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneCarrierSunk == False and playerOneCarrier == []:
                playerOneCarrierSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
            #it was a miss so it reveals it
            elif playerOneHiddenGrid[r + squaresOver][c] == "🟦":
              playerOneHiddenGrid[r + squaresOver][c] = "⬜"
              print("The computer's turn is over")
              turn += 1
              #if there is only one direction and the ship didn't sink then it has to be the other way so it swaps the direction
              if len(directions) == 1:
                squaresOver = 1
                directions = [1]
              #it hasn't found the right direction so it just removes down from possible directions
              else:
                directions.remove(direction)
                squaresOver = 1
            #makes sure the square has been attacked
            elif playerOneHiddenGrid[r + squaresOver][c] == "🟥" or playerOneHiddenGrid[r + squaresOver][c] == "⬜":
              squaresOver += 1
              #breakCount allows me to exit from a while loop continue loop that breaks the code
              breakCount += 1
              if breakCount > 10:
                breakCount = 0
                hit = False
              continue
            #it isn't a square on the grid
            else:
              raise IndexError
          #if it is right
          elif direction == 4:
            #moves the attacked square right the amount of squaresOver it is supposed to be and checks if it was a hit
            if playerOneHiddenGrid[r][c - squaresOver] == "⬛":
              playerOneHiddenGrid[r][c - squaresOver] = "🟥"
              #it was a hit so that direction is made the only option in directions
              directions = [direction]
              hit = True
              #removes it from its ship
              if [r, c + squaresOver] in playerOneDestroyer:
                playerOneDestroyer.remove([r, c + squaresOver])
              elif [r, c + squaresOver] in playerOneSubmarine:
                playerOneSubmarine.remove([r, c + squaresOver])
              elif [r, c + squaresOver] in playerOneCruiser:
                playerOneCruiser.remove([r, c + squaresOver])
              elif [r, c + squaresOver] in playerOneBattleship:
                playerOneBattleship.remove([r, c + squaresOver])
              elif [r, c + squaresOver] in playerOneCarrier:
                playerOneCarrier.remove([r, c + squaresOver])
              #checks if any boats are sunk
              if playerOneDestroyerSunk == False and playerOneDestroyer == []:
                playerOneDestroyerSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneSubmarineSunk == False and playerOneSubmarine == []:
                playerOneSubmarineSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneCruiserSunk == False and playerOneCruiser == []:
                playerOneCruiserSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneBattleshipSunk == False and playerOneBattleship == []:
                playerOneBattleshipSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
              if playerOneCarrierSunk == False and playerOneCarrier == []:
                playerOneCarrierSunk = True
                hit = False
                squaresOver = 1
                directions = [1, 2, 3, 4]
            #it was a miss so it reveals it
            elif playerOneHiddenGrid[r][c + squaresOver] == "🟦":
              playerOneHiddenGrid[r][c + squaresOver]= "⬜"
              print("The computer's turn is over")
              turn += 1
              #if there is only one direction and the ship didn't sink then it has to be the other way so it swaps the direction
              if len(directions) == 1:
                squaresOver = 1
                directions = [2]
              #it hasn't found the right direction so it just removes left from possible directions
              else:
                directions.remove(direction)
                squaresOver = 1
            #makes sure the square has been attacked
            elif playerOneHiddenGrid[r][c + squaresOver] == "🟥" or playerOneHiddenGrid[r][c + squaresOver] == "⬜":
              squaresOver += 1
              #breakCount allows me to exit from a while loop continue loop that breaks the code
              breakCount += 1
              if breakCount > 10:
                breakCount = 0
                hit = False
              continue
            ##it isn't a square on the grid
            else:
              raise IndexError
        #it wasn't on the grid so it resets the directions
        except IndexError:
          directions = [1, 2, 3, 4]
      #checks if game is won
      if playerOneDestroyerSunk == True and playerOneSubmarineSunk == True and playerOneCruiserSunk == True and playerOneBattleshipSunk == True and playerOneCarrierSunk == True:
        print(Fore.WHITE + "\t\tPlayer One\n\n")
        gridPrint(playerTwoGrid)
        print("\n\n")
        gridPrint(playerOneHiddenGrid)
        print("The computer won")
        time.sleep(1)
        menu()

#takes turns attacking
def game():
  global playerOneGrid
  global playerOneHiddenGrid
  global playerTwoGrid
  global playerTwoHiddenGrid
  global playerOneDestroyer
  global playerOneSubmarine
  global playerOneCruiser
  global playerOneBattleship
  global playerOneCarrier
  global playerTwoDestroyer
  global playerTwoSubmarine
  global playerTwoCruiser
  global playerTwoBattleship
  global playerTwoCarrier
  #initialized booleans
  playerOneDestroyerSunk = False
  playerOneSubmarineSunk = False
  playerOneCruiserSunk = False
  playerOneBattleshipSunk = False
  playerOneCarrierSunk = False
  playerTwoDestroyerSunk = False
  playerTwoSubmarineSunk = False
  playerTwoCruiserSunk = False
  playerTwoBattleshipSunk = False
  playerTwoCarrierSunk = False
  global turn
  #loop that runs until broken
  while True:
    os.system("clear")
    if turn % 2 == 0:
      print(Fore.WHITE + "\t\tPlayer One\n\n")
      gridPrint(playerTwoGrid)
      print("\n\n")
      gridPrint(playerOneHiddenGrid)
      choice = input("\n\nWhere would you like to attack?\n\n").split()
      #validates the coordinate
      if len(choice) == 2 and choice[0].isalpha() and choice[1].isdigit():
        letter = letter2Num(choice[0])
        number = int(choice[1])
        if letter == False or number > 10 or number < 1:
          print("Not valid\n\nMake sure it is a point on the grid")
          time.sleep(0.5)
        #checks if it is a hit
        elif playerTwoHiddenGrid[number][letter] == "⬛":
          #reveals hit square
          playerTwoGrid[number][letter] = "🟥"
          playerTwoHiddenGrid[number][letter] = "🟥"
          #removes the square from its ship
          if [number, letter] in playerTwoDestroyer:
            playerTwoDestroyer.remove([number, letter])
          elif [number, letter] in playerTwoSubmarine:
            playerTwoSubmarine.remove([number, letter])
          elif [number, letter] in playerTwoCruiser:
            playerTwoCruiser.remove([number, letter])
          elif [number, letter] in playerTwoBattleship:
            playerTwoBattleship.remove([number, letter])
          elif [number, letter] in playerTwoCarrier:
            playerTwoCarrier.remove([number, letter])
          print("That was a hit\n")
          time.sleep(1)
          #checks if any ships are sunk
          if playerTwoDestroyerSunk == False and playerTwoDestroyer == []:
            playerTwoDestroyerSunk = True
            print("You sunk the destroyer\n")
            time.sleep(1)
          if playerTwoSubmarineSunk == False and playerTwoSubmarine == []:
            playerTwoSubmarineSunk = True
            print("You sunk the submarine\n")
            time.sleep(1)
          if playerTwoCruiserSunk == False and playerTwoCruiser == []:
            playerTwoCruiserSunk = True
            print("You sunk the cruiser\n")
            time.sleep(1)
          if playerTwoBattleshipSunk == False and playerTwoBattleship == []:
            playerTwoBattleshipSunk = True
            print("You sunk the battleship\n")
            time.sleep(1)
          if playerTwoCarrierSunk == False and playerTwoCarrier == []:
            playerTwoCarrierSunk = True
            print("You sunk the carrier\n")
            time.sleep(1)
          #checks if game is won
          if playerTwoDestroyerSunk == True and playerTwoSubmarineSunk == True and playerTwoCruiserSunk == True and playerTwoBattleshipSunk == True and playerTwoCarrierSunk == True:
            print("You sunk all the ships\n")
            time.sleep(1)
            print("Player one wins")
            menu()
          print("You get to shoot again")
          time.sleep(1)
        #checks if it was miss
        elif playerTwoHiddenGrid[number][letter] == "🟦":
          #reveals missed square
          playerTwoGrid[number][letter] = "⬜"
          playerTwoHiddenGrid[number][letter] = "⬜"
          print("That was a miss")
          time.sleep(1)
          print("It is time to switch players")
          time.sleep(1)
          turn += 1
          os.system("clear")
          print(Fore.WHITE + "Player two press anything to continue")
          key = getkey()
        #square wasn't a miss or hit so it was attacked already
        else:
          print("You already attacked there")
          time.sleep(1)
      else:
        print("Not valid\n\nEnter like A 1") 
        time.sleep(2)
    else:
      print(Fore.WHITE + "\t\tPlayer Two\n\n")
      gridPrint(playerOneGrid)
      print("\n\n")
      gridPrint(playerTwoHiddenGrid)
      choice = input("\n\nWhere would you like to attack?\n\n").split()
      #validates input
      if len(choice) == 2 and choice[0].isalpha() and choice[1].isdigit():
        letter = letter2Num(choice[0])
        number = int(choice[1])
        if letter == False or number > 10 or number < 1:
          print("Not valid\n\nMake sure it is a point on the grid")
          time.sleep(0.5)
        #checks if it was a hit
        elif playerOneHiddenGrid[number][letter] == "⬛":
          #reveals hit square
          playerOneGrid[number][letter] = "🟥"
          playerOneHiddenGrid[number][letter] = "🟥"
          #removes the square from its ship
          if [number, letter] in playerOneDestroyer:
            playerOneDestroyer.remove([number, letter])
          elif [number, letter] in playerOneSubmarine:
            playerOneSubmarine.remove([number, letter])
          elif [number, letter] in playerOneCruiser:
            playerOneCruiser.remove([number, letter])
          elif [number, letter] in playerOneBattleship:
            playerOneBattleship.remove([number, letter])
          elif [number, letter] in playerOneCarrier:
            playerOneCarrier.remove([number, letter])
          print("That was a hit\n")
          time.sleep(1)
          #checks if any ships are sunk
          if playerOneDestroyerSunk == False and playerOneDestroyer == []:
            playerOneDestroyerSunk = True
            print("You sunk the destroyer\n")
            time.sleep(1)
          if playerOneSubmarineSunk == False and playerOneSubmarine == []:
            playerOneSubmarineSunk = True
            print("You sunk the submarine\n")
            time.sleep(1)
          if playerOneCruiserSunk == False and playerOneCruiser == []:
            playerOneCruiserSunk = True
            print("You sunk the cruiser\n")
            time.sleep(1)
          if playerOneDestroyerSunk == False and playerOneDestroyer == []:
            playerOneDestroyerSunk = True
            print("You sunk the battleship\n")
            time.sleep(1)
          if playerOneCarrierSunk == False and playerOneCarrier == []:
            playerOneCarrierSunk = True
            print("You sunk the carrier\n")
            time.sleep(1)
          #checks if game is won
          if playerOneDestroyerSunk == True and playerOneSubmarineSunk == True and playerOneCruiserSunk == True and playerOneBattleshipSunk == True and playerOneCarrierSunk == True:
            print("You sunk all the ships\n")
            time.sleep(1)
            print("Player two wins")
            menu()
          print("You get to shoot again")
          time.sleep(1)
        #checks if it was miss
        elif playerOneHiddenGrid[number][letter] == "🟦":
          #reveals missed square
          playerOneGrid[number][letter] = "⬜"
          playerOneHiddenGrid[number][letter] = "⬜"
          print("That was a miss")
          time.sleep(1)
          print("It is time to switch players")
          time.sleep(1)
          turn += 1
          os.system("clear")
          print(Fore.WHITE + "Player one press anything to continue")
          key = getkey()
        #square wasn't a miss or hit so it was attacked already
        else:
          print("You already attacked there")
          time.sleep(1)
      else:
        print("Not valid\n\nEnter like A 1") 
        time.sleep(2)

#allows user to choose what happens next
def menu():
  os.system("clear")
  choice = input(Fore.WHITE + "What would you like to do?\n\t1. Play\n\t2. Rules\n\t3. Quit\n")
  if choice == "1":
    setup()
  elif choice == "2":
    os.system("clear")
    print("This is battleship. In this game two player take turns guessing where each others ships are. The goal of the game is to sink your opponent's ships. In this game 🟦 represents water, ⬛ represents a ship, ⬜ represents a miss, and 🟥 represents a hit. You take turn guessing the format letter number (i.e. A 1) until one player wins. Godd luck")
    time.sleep(7)
    menu()
  elif choice == "3":
    sys.exit
  else:
    print(Fore.RED + "Not valid. Try again")
    menu()

#plays intro
def main():
  print('''                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  print('''\t                                     # #  ( )
  \t                                  ___#_#___|__
  \t                              _  |____________|  _
  \t                       _=====| | |            | | |==== _
  \t                 =====| |.---------------------------. | |====
  \t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
  \t     \                                                             /
  \t      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  print('''\t\t                                     # #  ( )
  \t\t                                  ___#_#___|__
  \t\t                              _  |____________|  _
  \t\t                       _=====| | |            | | |==== _
  \t\t                 =====| |.---------------------------. | |====
  \t\t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
  \t\t     \                                                             /
  \t\t      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  print('''\t\t\t                                     # #  ( )
  \t\t\t                                  ___#_#___|__
  \t\t\t                              _  |____________|  _
  \t\t\t                       _=====| | |            | | |==== _
  \t\t\t                 =====| |.---------------------------. | |====
  \t\t\t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
  \t\t\t     \                                                             /
  \t\t\t      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  print('''\t\t\t\t                                     # #  ( )
  \t\t\t\t                                  ___#_#___|__
  \t\t\t\t                              _  |____________|  _
  \t\t\t\t                       _=====| | |            | | |==== _
  \t\t\t\t                 =====| |.---------------------------. | |====
  \t\t\t\t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
  \t\t\t\t     \                                                             /
  \t\t\t\t      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  print('''\t\t\t\t\t                                     # #  ( )
  \t\t\t\t\t                                  ___#_#___|__
  \t\t\t\t\t                              _  |____________|  _
  \t\t\t\t\t                       _=====| | |            | | |==== _
  \t\t\t\t\t                 =====| |.---------------------------. | |====
  \t\t\t\t\t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
  \t\t\t\t\t     \                                                             /
  \t\t\t\t\t      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  print('''\t\t\t\t\t\t                                     # #  ( )
  \t\t\t\t\t\t                                  ___#_#___|__
  \t\t\t\t\t\t                              _  |____________|  _
  \t\t\t\t\t\t                       _=====| | |            | | |==== _
  \t\t\t\t\t\t                 =====| |.---------------------------. | |====
  \t\t\t\t\t\t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
  \t\t\t\t\t\t     \                                                             /
  \t\t\t\t\t\t      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  print('''\t\t\t\t\t\t\t                                     # #  ( )
  \t\t\t\t\t\t\t                                  ___#_#___|__
  \t\t\t\t\t\t\t                              _  |____________|  _
  \t\t\t\t\t\t\t                       _=====| | |            | | |==== _
  \t\t\t\t\t\t\t                 =====| |.---------------------------. | |====
  \t\t\t\t\t\t\t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
  \t\t\t\t\t\t\t     \                                                             /
  \t\t\t\t\t\t\t      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  print('''\t\t\t\t\t\t\t\t                                     # #  ( )
  \t\t\t\t\t\t\t\t                                  ___#_#___|__
  \t\t\t\t\t\t\t\t                              _  |____________|  _
  \t\t\t\t\t\t\t\t                       _=====| | |            | | |==== _
  \t\t\t\t\t\t\t\t                 =====| |.---------------------------. | |====
  \t\t\t\t\t\t\t\t   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
  \t\t\t\t\t\t\t\t     \                                                             /
  \t\t\t\t\t\t\t\t      \___________________________________________________________/''')
  time.sleep(0.2)
  os.system("clear")
  menu()

main()