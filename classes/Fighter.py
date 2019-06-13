import random

class Fighter():
  def __init__(self,name):
    self.name = name
    self.maxHealth = 120
    self.currentHealth = self.maxHealth
    self.attackUp = 2
    self.attack = (random.randint(1,6) + self.attackUp)
    self.attackStr = "1D6"
    self.attackName = "Slash your sword"
    self.attackHit = ("You slash the enemy with your sword!!!")
    self.attackMiss = ("You miss the enemy with your sword!!!")
    self.gold = 0
    self.potion = 2
    self.scroll = 0
    self.scrollAttack = random.randint(1,20)