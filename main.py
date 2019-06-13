import sys
import os
import random
import pickle

from classes.Enemy import Enemy
from classes.Fighter import Fighter
from classes.Ranger import Ranger
from classes.Wizard import Wizard

def mainMenu():
	os.system('clear')
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("    Welcome to Dungeon Crawl!!!    ")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print("1. Start")
	print("2. Load")
	print("3. Quit")

	option = input(" ")

	if option == "1":
		choosePlayer()
	elif option == "2":
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		nameOfFile = input("What was the name of the adventurer you would like to load?: ")
		if os.path.exists(nameOfFile) == True:
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
			PlayerIG = pickle.load(open(nameOfFile, "rb"))
			print("Loaded saved state...")
			option = input(" ")
			continueGame()
		else:
			print("There is not a save file named that!")
			option = input(" ")
			mainMenu()
	elif option == "3":                                                              
		sys.exit
	else:
		mainMenu()

def choosePlayer():
	os.system('clear')
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("        Choose your player     		")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print("1. Fighter")
	print("2. Wizard")
	print("3. Ranger")

	option = input(" ")
	name = input("\nWhat is your Name Traveler?: \n")

	if option == "1":
		PlayerIG = Fighter(name)
	elif option == "2":
		PlayerIG = Wizard(name)
	elif option == "3":
		PlayerIG = Ranger(name)
	else:
		choosePlayer()
	continueGame(PlayerIG)

def continueGame(player):
	os.system('clear')
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("            The Town 			    		")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print(("%s's Stats and Inventory:") % (player.name))
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print(("HP: %i/%i") % (player.currentHealth, player.maxHealth))
	print(("Attack: %s + %i from bonus") % (player.attackStr, player.attackUp))
	print(("Gold: %i") % (player.gold))
	print(("Potions: %i") %(player.potion))
	print(("Scrolls: %i || 1D20 Damage\n") % (player.scroll))
	print(("\nWhat would you like to do %s?") % (player.name))
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print("1. Explore the Dungeon")
	print("2. Drink a Potion")
	print("3. Go to the Shop\n\n\n")
	print("4. Save the Game")
	print("5. Main Menu")
	option = input(" ")
	if option == "1":
		roomGen(player)
	elif option == "2":
		drinkPotion(player)
		continueGame(player)
	elif option == "3":
		store()
	elif option == "4":
		pickle.dump(player, open(player.name, "wb"))
		print("\nGame has been saved!\n")
		option = input(" ")
		continueGame(player)
	elif option == "5":
		mainMenu()
	else: 
		continueGame(player)

def roomGen(player):
	roomType = random.randint(1,10)
	if 1 <= roomType <= 6:
		emptyRoom(player)
	elif 7 <= roomType <= 8:
		fight(preFight(), player)
	else:
		foundChest(player)

def emptyRoom(player):
	os.system('clear')
	print("\n")
	emptyRoomGen = random.randint(1,20)
	if emptyRoomGen == 1:
		print("You enter a room that is completely barren.")
		option = input(" ")
	elif emptyRoomGen == 2:
		print("You enter a room that has barrels and crates. It looks like a storage room of sorts.")
		option = input(" ")
	elif emptyRoomGen == 3:
		print("You enter a room that has a fountain in the middle.")
		option = input(" ")
	elif emptyRoomGen == 4:
		print("You enter a room that has a shrine to a god that you do not recognize.")
		option = input(" ")
	elif emptyRoomGen == 5:
		print("You enter a room that contains a statue that bears an eerie resemblance to yourself.")
		option = input(" ")
	elif emptyRoomGen == 6:
		print("You found a skeleton!")
		option = input(" ")
		print("Just a regular skeleton… In a room with nothing else.")
		option = input(" ")
	elif emptyRoomGen == 7:
		print("You enter a room that contains crudely constructed gym equipment.")
		option = input(" ")
	elif emptyRoomGen == 8:
		print("You enter a room that contains a hat salesman.")
		option = input(" ")
	elif emptyRoomGen == 9:
		print("You enter a room that is only a 3 foot wide walkway with chasms on each side extending farther down than you can see.")
		option = input(" ")
	elif emptyRoomGen == 10:
		print("You enter a room with several obvious counterfeit gold pieces covering the floor.")
		option = input(" ")
	elif emptyRoomGen == 11:
		print("You enter a room that has an ungodly amount of cobwebs.")
		option = input(" ")
	elif emptyRoomGen == 12:
		print("You enter a room with a bag of sand gently balanced on a pedestal.")
		option = input(" ")
	elif emptyRoomGen == 13:
		print("You enter a room that has a throne in the middle. This was obviously the throne room to a once great king.")
		option = input(" ")
	elif emptyRoomGen == 14:
		print("You enter a room that contains a plethora of the finest cleaning supplies. This was obviously the janitor’s closet for a janitor of a once great king.")
		option = input(" ")
	elif emptyRoomGen == 15:
		print("You enter a room that is filled with coffins for warriors of a great army.")
		option = input(" ")
	elif emptyRoomGen == 16:
		print("You enter a room that contains a perfect clone of yourself. Upon closer inspection it appears to simply be a well polished mirror.")
		option = input(" ")
	elif emptyRoomGen == 17:
		print("You enter a room that is super bright. Upon closer inspection there is just a torch on the wall.")
		option = input(" ")
	elif emptyRoomGen == 18:
		print("You enter a room. The walls are covered in the scrawlings of a strange, unknown language. Reading it makes your head spin.")
		option = input(" ")
	elif emptyRoomGen == 19:
		print("You enter a room that looks to be a wizards old laboratory. There are messy notes and glass beakers everywhere.")
		option = input(" ")
	else:
		print("You enter an unreasonably long hallway.")
		option = input(" ")

	stillExplore(player)

def preFight():
	os.system('clear')
	print("\n")
	enemyChance = random.randint(1,100)
	if enemyChance <= 2:  #2% Dragon Spawn
		enemy = Enemy("Dragon", 60, { "low": 1, "high": 20 }, { "low": 80, "high": 160 })
		print("Like a comet, a dragon flys into the ground creating a \nshockwave as it does so... its ready to take you down!")
		option = input(" ")
	elif 3 <= enemyChance <= 12: #10% Bandit Spawn
		enemy = Enemy("Bandit", 25, { "low": 1, "high": 12 }, { "low": 15, "high": 70 })
		print("From the shadows a bandit steps out... He looks ready to \ntake your gold, killing you in the process if necessary.")
		option = input(" ")
	elif 13 <= enemyChance <= 27: #15% Orc Spawn
		enemy = Enemy("Orc", 20, { "low": 1, "high": 10 }, { "low": 15, "high": 60 })
		print("You found an orc!")
		option = input(" ")
	elif 28 <= enemyChance <= 47: #20% Goblin Spawn
		enemy = Enemy("Goblin", 15, { "low": 1, "high": 8 }, { "low": 5, "high": 40 })
		print("You found a goblin!")
		option = input(" ")
	elif 48 <= enemyChance <= 71: #24% Skeleton Spawn
		enemy = Enemy("Skeleton", 10, { "low": 1, "high": 6 }, { "low": 4, "high": 25 })
		print("You found a skeleton!")
		option = input(" ")
	else: #29% Zombie Spawn
		# TODO: Zombie wasnt defined, so I copied Skeleton
		enemy = Enemy("Zombie", 10, { "low": 1, "high": 6 }, { "low": 4, "high": 25 })
		print("You found a zombie!")
		option = input(" ")

	return enemy;

def foundChest(player):
	os.system('clear')
	print("\n")
	print("You found a chest do you want to open it?")
	print("1. Yes")
	print("2. No")
	option = input(" ")
	if option == "1":
		chestRoom(player)
	else:
		stillExplore(player)

def chestRoom(player):
	os.system('clear')
	print("\n")
	chestGen = random.randint(1,5)
	if chestGen == 1:
		if player.potion == 5:
			print("You found a potion but dont have any room would \nyou like to drink it?")
			print("1. Yes")
			print("2. No")
			option = input(" ")
			if option == "1":
				drinkPotion(player)
				roomGen(player)
			else:
				print(" ")
		else:
			player.potion += 1
			print("You found a potion!")
	elif chestGen == 2:
		player.attackUp += 1
		print("You open the chest and it's empty...")
		option = input(" ")
		print("Next thing you know your sword starts glowing! It seems to have been imbued with magic: \nYour sword just became stronger!!! || +1 to your current damage.")
	elif chestGen == 3:
		chestGold = random.randint(10,200) 
		player.gold += chestGold
		print("You open the chest and gold fills your eyes!!!\nYou just found " + str(chestGold) + " Gold!!!")
	elif chestGen == 4:
		if player.scroll == 3:
			print("you found a scroll but you dont have room for it")	
		else:
			player.scroll += 1
			print("You found a scroll")	
	else:
		 print("You try and open the chest...")
		 option = input(" ")
		 print("Next thing you know the chests eyes open!!!")
		 option = input(" ")
		 print("Its a mimic and before you know it makes an attack at you!")
		 option = input(" ")
		 player.currentHealth -= mimic.attack
		 enemy = Enemy("Mimic", 35, { "low": 1, "high": 14 }, { "low": 100, "high": 100 })
		 fight(enemy, player)

	option = input(" ")
	stillExplore(player)

def fight(enemy, player):
	os.system('clear')
	print("\n")
	print (("%s's HP: %i/%i     %s's HP:%i/%i") % (player.name, player.currentHealth, player.maxHealth, enemy.name, enemy.currentHealth, enemy.maxHealth))
	print("\nInventory:")
	print("~~~~~~~~~~~~")
	print(("Scrolls: %i") % (player.scroll))
	print(("Potions: %i") % (player.potion))
	print("\n\nActions:")
	print("~~~~~~~~~~~~")
	print(("1. %s") % (player.attackName))
	print("2. Use Scroll")
	print("3. Drink Potion")
	print("4. Run")
	option = input(" ")
	if option == "1":
		attack(enemy, player)
	elif option == "2":
		scrollAttack(enemy, player)
	elif option == "3":
		drinkPotion()
		fight(enemy, player)
	elif option == "4":
		run(enemy, player)
	else:
		fight(enemy, player)

def attack(enemy, player):
	os.system('clear')
	print("\n")
	playerHit = random.randint(1,2)
	enemyHit = random.randint(1,2)
	if playerHit == 1:
		print(("%s") % ( player.attackHit))
		enemy.currentHealth -= (player.attack + player.attackUp)
	else:
		print(("%s") % ( player.attackMiss))
		 
	option = input(" ")

	if enemyHit == 1:
		print (("The %s hit you!!!") % ( enemy.name))
		player.currentHealth -= enemy.attack
	else:
		print(("The %s missed you!!!") % ( enemy.name))

	option = input(" ")

	resolve(enemy, player)

def scrollAttack(enemy, player):
	os.system('clear')
	print("\n")
	if player.scroll == 0:
		print("You don't have any scrolls left!")
		option = input(" ")
		Fight()
	else:
		print(("You read the scroll conjuring forth a fireball blasting the %s!!!") % (enemy.name))
		enemy.currentHealth -= player.scrollAttack
		player.scroll -= 1
		option = input(" ")
		resolve(enemy, player)

def drinkPotion(player):
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	if player.currentHealth == player.maxHealth:
		print("You dont need to use a potion!")
		option = input(" ")
	elif player.potion == 0:
		print("You dont have any potions left!")
		option = input(" ")
	else:
		healthReceived = (random.randint(1,10) + random.randint(1,10) + 5)
		player.currentHealth += healthReceived
		print(("You gained %i health!") % (healthReceived))
		player.potion -= 1
		option = input(" ")
		if player.currentHealth >= player.maxHealth:
			player.currentHealth = player.maxHealth

def run(enemy, player):
	getAway = random.randint(1,3)
	if random.randint(1,3) == 1:
		print("\nYou got away!")
		option = input(" ")
		continueGame(player)
	else:
		print("\nYou didn't get away!")
		print (("The %s hit you!!!") % ( enemy.name))
		player.currentHealth -= enemy.attack
		option = input(" ")
	resolve(enemy, player)
	
def resolve(enemy, player):
	os.system('clear')
	print("\n")
	if player.currentHealth <= 0:
		print("You Died...")
		option = input(" ")
		os.system('clear')
		if player.gold == 0:
			print("I didn't think it was possible... you found literally 0 gold...")
			sys.exit
		else:
			print(("At least you found %i gold coins in your adventure!") % (player.gold))
			sys.exit
	if enemy.currentHealth <= 0:
		print(("You killed the %s") % (enemy.name))
		enemy.currentHealth = enemy.maxHealth
		player.gold += enemy.goldGain
		print(("You found %i gold on the %s") % (enemy.goldGain, enemy.name))
		option = input(" ")
		stillExplore(player)
	else:
		fight(enemy, player)

def store(player):
	os.system('clear')
	print(("Welcome to my shop %s! What would you like?\n") % (player.name))
	print("Your Inventory:")
	print(("Gold: %i") % (player.gold))
	print(("Scrolls: %i") % (player.scroll))
	print(("Potions: %i") % (player.potion))
	print("\nThe Shops Inventory:")
	print("1. 1 Potion || Cost: 30 Gold")
	print("2. 1 scroll || Cost: 50 Gold")
	print("3. Leave Store")
	option = input(" ")
	if option == "1":
		if player.gold < 30:
			print("Sorry you dont have enough for a potion.")
			option = input(" ")
		elif player.potion > 5:
			print("Sorry it doesnt look like you have any more room for potions.")
			option = input(" ")
		else:
			print("Thank you for your purchase. Here is the potion!")
			option = input(" ")
			print("You have gained 1 potion!!!")
			option = input(" ")
			player.potion += 1
			player.gold -= 30
		store()
	elif option == "2":
		if player.gold < 50:
			print("Sorry you dont have enough for a scroll.")
			option = input(" ")
		elif player.scroll > 3:
			print("Sorry it doesnt look like you have any more room for a scroll.")
			option = input(" ")
		else:
			print("Thank you for your purchase. Here is the scroll!")
			option = input(" ")
			player.scroll += 1
			player.gold -= 50
		store()
	elif option == "3":
		print("Alrighty! have a nice day!")
		option = input(" ")
		continueGame(player)
	else:
		store(player)

def stillExplore(player):
	os.system('clear')
	print("\n")
	print("1. Keep Exploring the Dungeon")
	print("2. Go Back to Town")
	option = input(" ")
	if option == "1":
		roomGen(player)
	elif option == "2":
		continueGame(player)
	else:
		stillExplore(player)

mainMenu()