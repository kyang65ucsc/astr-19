def f(x):
	return x**3+8
	
def main():
	x = 9
	y = f(x)
	print('x**3+8 =',y)
	if (y > 27):
		print('YAY!')
	else:
		print('nah')

if __name__=="__main__":
	main()