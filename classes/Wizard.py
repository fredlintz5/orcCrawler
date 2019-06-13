import random

class Wizard():
  def __init__(self,name):
    self.name = name
    self.maxHealth = 80
    self.currentHealth = self.maxHealth
    self.attackUp = 2
    self.attack = (random.randint(1,10) + self.attackUp)
    self.attackStr = "1D10"
    self.attackName = "Cast Firebolt"
    self.attackHit = ("You blast the enemy with a bolt of fire!!!")
    self.attackMiss = ("The bolt of fire whizzes past the enemy!!!")
    self.gold = 0
    self.potion = 2
    self.scroll = 1
    self.scrollAttack = random.randint(1,20)