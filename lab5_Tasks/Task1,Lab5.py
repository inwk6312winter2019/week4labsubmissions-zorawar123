from math import sqrt
class Point(): # declear class
    pass # Pass Fuction will continue next staemnets and will terminate from class withot throwing error.

C=Point() # C is the object of point class 
C.p1=(5,6) # passsing argumnets in class Parameter
C.p2=(9,10)# passsing argumnets in class Parameter

def Distance(P1,P2):
	distance=sqrt((P2[0]-P1[0])**2+(P2[1]-P1[1])**2)
	print(distance)
Distance(C.p1,C.p2)
