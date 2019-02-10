class Point():

	def __init__(self,x,y):
		self.x=x
		self.y=y
	
	def __add__(self,self2):
		if isinstance(self2,Point):
			sum=(self.x+self2.x,self.y+self2.y)
			return sum
		else:
			sum=(self.x+self2[0],self.y+self2[1])
			return sum
p1=Point(3,4)
p2=Point(7,3)
print(p1 + (4,5))
print(p1 + p2)
