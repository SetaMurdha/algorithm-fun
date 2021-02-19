import math
def Lingkaran(radius):
	#luas lingkaran = pi * r^2
	hasil = math.pi * (radius ** 2) 
	return hasil

def PersegiPanjang(Height, Weight):
	#luas PersegiPanjang = Height * Weight
	hasil = Height * Weight
	return hasil

def Persegi(Length):
	#luas Persegi = Line^2
	hasil = Length**2
	return hasil

def Segitiga(Base, Height):
	hasil = int((Base * Height)/2)
	return hasil

if __name__ == '__main__':
	print(Segitiga(2,2))
	