game = [[0,0,0],
		[0,0,0],
		[0,0,0]]

print("   a  b  c")
for count, row in enumerate(game):
	print(count, row)


game[0][2] = 1

print("   a  b  c")
for count, row in enumerate(game):
	print(count, row)
