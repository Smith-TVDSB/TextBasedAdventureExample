import time
import random

def startingRoom ():
	print("You find yourself in a room with only one way forward, what do you do?")
	command = input("Walk forward (w), walk back (s), walk left (a), or walk right(d)\n") #TODO: clean this up
	if command.lower() == "w":
		secondRoom()
	else:
		print("You hit a wall, start over")
		startingRoom()


def secondRoom():
	print("You're in a hallway, you can walk forward or back")
	if not (haveKey) : #Bug, this will let us grab an infinite amount of keys
		print("There is a key on the ground, you may pick it up (p)")
	command = input("Walk forward (w), walk back (s), walk left (a), or walk right(d)\n").lower() #TODO: clean this up
	if command== 'p':
		haveKey = True #picked up the key
		#TODO remove key from ground
		secondRoom()
	elif command=='w':
		cornerRoom()
	elif command=='s':
		startingRoom()
	else:
		print("Invalid option, start over.")

def cornerRoom ():
	print("You reach the end of the hall, to your left (a), is a locked door")
	command = input("Walk forward (w), walk back (s), walk left (a), or walk right(d)\n") #TODO: clean this up
	if command.lower()=='a' and haveKey: 
		haveKey = False #used the key so it breaks
		finalRoom()
	elif command.lower()=='s':
		secondRoom()
	else:
		print("Invalid option, start over.")

def finalRoom ():
	print("The door slams shut behind you as a mechanism slides bars infront of it.")
	for i in range(3):
		time.sleep(1)
		print(". ")
	print("You're locked in")
	time.sleep(3)
	print("You hear some slushy wet noise from the ceiling, you look up to only watch a green blob drop")
	print("Prepare for battle! The slime charges you. (t) to attack, (r) to run away")
	command = input().lower()
	if command=='t':
		print("You draw your bow and then throw the canvas at it.")
		attack = random.randint(1,6)
		print("You deal", attack,"damage to the slime!")
		if (attack >=3):
			print ("You defeated the slime! You win")
		else:
			print ("The slime disolves the paper you threw at it,")
			time.sleep(1)
			print("Now you're next\n GAME OVER")
	else:
		print ("You tripped and fell only to wake from a horrible dream of being lost in a text based adventure")

#DECLARE GLOBAL VARIABLES
global haveKey
#SET GLOBAL VALUES BEFORE GAME START
haveKey = False

#GAME START
startingRoom()
