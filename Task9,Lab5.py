class Vehicle:
	pass
class LandVehicle(Vehicle):
	pass
class TrackedVehicle(LandVehicle):
	pass
for i in [Vehicle, LandVehicle, TrackedVehicle]:
	for j in [Vehicle, LandVehicle, TrackedVehicle]:
		print(issubclass(i,j), sep = " \t ")
	print()