#ZOMBIE TEXT GAME
from sys import exit
import time

#BACKEND STATS
inventory = ['flashlight']
playerHealth = 100
hatchetAttack = 15
zombieHealth = 20
zombieAttack = 10


#AREAS AND LEVELS
#STARTING FIELD
def startField():
	global inventory
	print "\nENTERING: FIELD..."
	time.sleep(1)
	print("""\n\tYou've awoken in an empty field. You see a barn in the distance. There is 
	a stump nearby with a hatchet lodged into it. Take the hatchet?""")
	
	#ask user if they want to pick up the hatchet
	pickup = raw_input("> ")
	if pickup == 'yes' or pickup == 'y':
		#adds hatchet to inventory list
		addToInventory(['hatchet'])
		print "\n\t%s: This could come in handy..." % playerName
		print "\n\tYou've acquired a HATCHET!"
	#if they choose not to pick up the hatchet
	else:
		print "\n\t%s:Ha!..what would I need a hatchet for? \n\tYou leave the hatchet in the stump." % playerName
	

	#lets the user know what the contents of their inventory
	print "\nYour inventory contains: %s" % inventory

	#move to outside the barn area
	print "\n1. Walk towards the barn. \n2. Stay and wait for rescue."
	move = raw_input("> ")
	if move == "1":
		areaBarn()
	else:
		print "You decide to stay and wait for rescue, but nobody comes for you."
		dead()


#OUTSIDE THE BARN
def areaBarn():
	global inventory
	global hatchetAttack
	#story
	print("""\n\tYou reach an old barn. It appears to have been abandoned for quite some time.
	As you approach the barn, you notice a wretched smell. The smell grows stronger, and you
	begin to feel nauseous.""")
	#decision time
	print "\n1. Enter the barn.\n2. Search the area."
	

	choice = raw_input("> ")
	if choice == "1":
		#enter the barn area
		print "You enter the barn"
		insideBarn()

	elif choice == "2": #if they search the area they will find a hidden item WATER
		print "You search the surrounding area. You find WATER!"
		addToInventory(["water"]) #adds WATER to inventory
		print "Your inventory contains: %s" % inventory
		print "Entering the barn..."
		#wait 1 seconds
		time.sleep(1)
		insideBarn()

	else:
		print "Please choose '1' to enter the barn, or '2' to search the area."


#INSIDE THE BARN
def insideBarn():
	#variables we need to use
	global playerHealth
	global zombieAttack
	global zombieHealth
	global hatchetAttack
	print "\nENTERING: BARN..."
	time.sleep(2)
	#STORY
	print "\t%s: Holy shit, a ZOMBIE! A real live...er...undead zombie! \n\tThe zombie lunges towards you!" % playerName

	#check if the player has the hatchet in their inventory
	time.sleep(2)

	if 'hatchet' in inventory:	#if they do, run this
		print "\nUse your hatchet to attack!"
		print "\n1. Attack \n2. Try to flee \n"
		attack = raw_input("> ")

		#if player chooses to attack:
		if attack == "attack" or 1:
			while zombieHealth > 0 and playerHealth > 0:
				#zombie attacking
				playerHealth -= zombieAttack
				print "\n\tThe zombie hits %s for 10!" % playerName
				print "\n\tYour health drops by %d!" % zombieAttack

				#player attacking
				zombieHealth -= hatchetAttack
				#make zombieHealth always 0
				if zombieHealth < 0:
					zombieHealth = 0
				print "\n\t%s hits the zombie for %d. Zombie has %d health remaining!" % (playerName, hatchetAttack, zombieHealth)
				time.sleep(.5)

			if zombieHealth <= 0:
				print "\n\tThe zombie is dead! Good job! You live with %d health." % (playerHealth)
				time.sleep(.75)

			elif playerHealth <= 0:
				print "You died."
				dead()

		#if player chooses to flee:
		elif attack == "flee" or 2:
			print "You try to run away!"
			print """\nZOMBIE: BRAAAIINNSSS!! \nThe zombie attacks you!"""
			playerHealth -= zombieAttack
			print "The zombie hits you for %d!" (zombieAttack)
			
	
	else: #if they don't have the hatchet, run this
		print "\nWithout a HATCHET to defend yourself, the zombie ruthlessly attacks you!"
		print "\n\tZombie: 'BRAAAIINNSSS!!'"
		while playerHealth > 0:
			playerHealth -= zombieAttack*2
			print "\n\tZombie hits you for %d!" % (zombieAttack*2)
			time.sleep(.5)
		if playerHealth <= 0:
			dead()

	print "\nYou found MALT, YEAST, HOPS, AND SUGAR!"
	addToInventory(['malt', 'yeast', 'hops', 'sugar'])
	print "\nYour inventory contains: %s" % inventory
	beer_check = raw_input("\nAttempt to craft beer? \n1. Yes\n2. No\n >")
	if beer_check == "yes" or 1:
		craftBeer()
		field_to_House()
	else:
		exit(0)
		fieldHouse()

#FIELD CONNECTING BARN AND HOUSE
def field_to_House():
	print "\nENTERING: FIELD..."
	time.sleep(2)
	print """\n\tOutside the barn you find a small path through the forest. 
	When you emerge, you see a small blue house. You begin walking towards the house."""
	print "\n1. Continue walking.\n2. Search the area."
	

	choice = raw_input("> ")
	if choice == "1":
		#enter the barn area
		print "You continue walking"
		field_to_House2()

	elif choice == "2": #if they search the area they will find a hidden item WATER
		if 'water' in inventory:
			print "Hm, nothing to find here."
		else:
			print "You search the surrounding area. You find WATER!"
			addToInventory(["water"]) #adds WATER to inventory
			print "Your inventory contains: %s" % inventory
			#wait 1 seconds
			time.sleep(1)
			beer_check = raw_input("\nAttempt to craft beer? \n1. Yes\n2. No\n >")
			if beer_check == "yes" or 1:
				craftBeer()
				field_to_House()
			else:
				exit(0)
				fieldHouse()
	else:
		print "Please choose '1' to enter the barn, or '2' to search the area."

	field_to_House()


#PLAYER FUNCTIONS
def addToInventory(items):
	global inventory
	inventory.extend(items)

def attack():
	global playerHealth
	global zombieHealth
	global zombieAttack
	playerHealth -= zombieAttack

def playerAttack(item, target):
	global hatchetAttack
	target -= item

def dead():
	print "\nYou have died. X_X"
	exit(0)

def craftBeer():
	beer_ingredients = ['water','malt','yeast','hops','sugar']
	global inventory
	if set(beer_ingredients).issubset(inventory):
		inventory = [x for x in inventory if x not in beer_ingredients]
		addToInventory(['beer'])
		print "You received BEER!"
		print inventory
	else:
		missing_items = [x for x in beer_ingredients if x not in inventory]
		print "You are missing an ingredient! %s!" % missing_items

#START OF GAME

print """\n\tWelcome PLAYER to the Zombie Text-Adventure Game!
	First, please enter your name:"""
global playerName
playerName = raw_input("> ")

print "\nPrepare for a spooky adventure, %s!" % playerName
print "%s: 2spooky4me..." % playerName

startField()
