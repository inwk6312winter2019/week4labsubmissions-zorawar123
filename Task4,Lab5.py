
class Time():
        hrs=11  # Variables defdine 
        min=12
        sec=38
time1=Time() # 
time2=Time()
time2.hrs=9
time2.min=8
time2.sec=48
def print_time(t):
        return ('The time is - {:}:{:}:{:}'.format(t.hrs,t.min,t.sec)) #  Format will  put hrs , min , secd before comma into {} 


t1=print_time(time1)
t2=print_time(time2)
print(t1)
print(t2)

def greater(n1,n2):
	return(n1 > n2) # will compare the dictionarys
print(greater(t1,t2))
