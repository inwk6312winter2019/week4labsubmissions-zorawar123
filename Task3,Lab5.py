class Time():
	hrs=2
	mins=12
	secs=38
time=Time() # object created 

def print_time(t):
	return('The time is - {:}:{:}:{:}'.format(t.hrs,t.mins,t.secs)) #  Format will  put hrs , min , secd before comma into {} 

print(print_time(time))

