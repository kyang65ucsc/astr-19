import sys

class FavoriteAnimal:
	def print(self):
		print('characteristics of FavoriteAnimal')
		print(f'arm length:{self.arm_length}')
		print(f'leg length:{self.leg_length}')
		print(f'number of eyes:{self.num_eyes}')
		print(f'does it have tail:{self.tail}')
		print(f'is it furry:{self.furry}')

	def __init__(self,alength = 22.0,llength = 22.0,neyes = 2,ttail = True,ffurry = True):
		self.arm_length = alength
		self.leg_length = llength
		self.num_eyes   = neyes
		self.tail       = ttail
		self.furry		= ffurry

def main():

	myfavanimal = FavoriteAnimal(22.0,22.0,2,True,True)
	myfavanimal.print()
if __name__=="__main__":
	main()