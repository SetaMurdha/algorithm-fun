
def Mainkan():
	i = 5
	j = 0
	for bilangan in range(0,i):
		for bilangan1 in range(j,5):
			print("*", end="")
		print("")
		j+=1

def Mainkan2():
	for bilangan in range(0,5):
		for bilangan in range(0,5):
			print("*",end="")
		print("")

def Mainkan3():
	i = 0
	j = 5
	for bilangan in range(0,5):
		for bilangan in range (i,5,1):
			print("*",end="")
		print("")
		i+=1
	for bilangan in range(0,5):
		for bilangan in range(j,6,1):
			print("*",end="")
		print("")
		j-=1

if __name__ == '__main__':
	Mainkan3()