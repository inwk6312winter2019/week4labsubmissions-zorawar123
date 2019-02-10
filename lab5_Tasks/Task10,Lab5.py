class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass
vehicle = Vehicle() #  Object created 
landvehicle = LandVehicle()  #  Object created 
trackedvehicle = TrackedVehicle() #  Object created 

for ob in [vehicle, landvehicle, trackedvehicle]:
	for cl in [Vehicle, LandVehicle, TrackedVehicle]:
		print(isinstance(ob,cl),end='\t') # isinstance() will  checks the object first argument and an instance of classinfo class
	print()
