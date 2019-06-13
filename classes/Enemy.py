import random

class Enemy():
	def __init__(self, name, maxHealth, attack, goldGain):
		self.name = name
		self.maxHealth = maxHealth
		self.currentHealth = self.maxHealth
		self.attack = random.randint(attack['low'],attack['high'])
		self.goldGain = random.randint(goldGain['low'],goldGain['high'])