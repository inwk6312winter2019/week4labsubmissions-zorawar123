class Rectangle():
	c1=(11,11)
P=Rectangle() # object created 

class rectangle():
	width=20
	height=20
	corner=P.c1
rec=rectangle() # object created 

def find_center(box):
	x=(rec.corner[0]+rec.width)/2
	y=(rec.corner[1]+rec.height)/2
	return(('Centre',(x,y)))
print(find_center(rec))
