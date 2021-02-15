game = [[0,0,0],
		[0,0,0],
		[0,0,0]]

def field_board(row=0, collumn=0, result=0, just_display  = False):
	print("   a  b  c")
	if not just_display:
		game[row][collumn] = result
	for count, row in enumerate(game):
		print(count, row)

field_board(1,1,5)

field_board(1,2,5)

field_board(1,0,5)

field_board(just_display = True)

