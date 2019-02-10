class Point():
	def __init__(self,x,y): # init is automatic assign when we create a variable 
		self.x=x
		self.y=y
	def __str__(self):
		return(f'({self.x},{self.y})')

	def __add__(self,self2): # 
		sum=(self.x+self2.x,self.y+self2.y)
		return(sum)

p1=Point(3,4)
p2=Point(5,6)
print(p1+p2)
