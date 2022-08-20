
def eqn(x,y,a,b,r):

	var = (x-a)^2 + (y-b)^2
	if(var>r^2):
		print('The point x,y is outside the circle')
	elif(var==r^2):
		print('The given point x,y is on the circle')
	else:
		print('The point is inside the circle')

eqn(0,0,2,2,5)