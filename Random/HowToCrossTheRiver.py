def introduction():
	Intro = """

A farmer with a fox, a goose, and a sack of corn needs to cross a river. The farmer
has a rowboat, but there is room for only the farmer and one of his three items. Unfortunately,
both the fox and the goose are hungry. The fox cannot be left alone with the
goose, or the fox will eat the goose. Likewise, the goose cannot be left alone with the
sack of corn, or the goose will eat the corn. How does the farmer get everything
across the river?

	"""
	return Intro

def die():
	print('Game Over')


def pickSomething():
	print('Wanna pick something before you go back?')

def pickedItem():
	PickedItem = input("Pick = Goose? Fox? Corn")
	return PickedItem
def main():

# Project pending

if __name__ == '__main__':
	main()