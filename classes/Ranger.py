import random

class Ranger():
  def __init__(self,name):       
    self.name = name
    self.maxHealth = 100
    self.currentHealth = self.maxHealth
    self.attackUp = 2
    self.attack = (random.randint(1,8) + self.attackUp)
    self.attackStr = "1D8"
    self.attackName = "Shoot your bow"
    self.attackHit = ("You pierce your enemy with an arrow from your bow!!!")
    self.attackMiss = ("The arrow whizzes by the enemy's head!!!")
    self.gold = 50
    self.potion = 2
    self.scroll = 0
    self.scrollAttack = random.randint(1,20)