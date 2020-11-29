import random

class playingDices:
	def __init__(self,x):
		self.x = x
	def playDices(self):
		print("Your dice = ", self.x)
		print("Dice is rolling...")
		hasil = random.randint(1,6)
		print("Dices = ",hasil)
		if self.x == hasil:
			print("You won")
		else:
			print("You lose") 

if __name__ == '__main__':
	yourInput = input("Masukkan taruhanmu (1 - 6) = ")
	op = playingDices(yourInput)
	op.playDices()