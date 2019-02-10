class kangro():
	def __init__(self,pouch1=None):
		if pouch1==None:
			pouch1=[]
		self.pouch1=pouch1
	def pouch2(self,self1):
		self.pouch1.append(self1)
	def __str__(self):
		return f'The pouch contains {self.pouch1}'
kanga=kangro()
roo=kangro()
kanga.pouch2('ready')
kanga.pouch2('go')

roo.pouch2('000')
kanga.pouch2(roo)

print(kanga)

print(kanga)
