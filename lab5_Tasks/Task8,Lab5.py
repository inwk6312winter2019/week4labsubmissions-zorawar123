class Point:
    def __init__(self,x=0,y=0):
        self.x= x # self is assign as a constructor which will assign automatically when we invoke the class
	    self.y= y
	def __str__(self):
        return(" ({},{})".format(self.x,self.y)) # format will assign the value of x in {} and print the value of x and gy

	def __add__(self,other):
		print (self.x+other.x,self.y+other.y)
	def add(self,other):
		if isinstance(other,tuple): # Check the object other is an instance or subclass of  object self, it will return true or
            print(self.x+other[0],self.y+other[1])
		else:
			print(self+other)


p1=Point(5,10)
p2=Point(10,15)
print(p1)
print(p2)
p1.add(p2)
p1.add((10,15))