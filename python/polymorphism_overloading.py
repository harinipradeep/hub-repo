class Sum:
	def add(self, a, b, c = None):
		if c:
			# add three numbers
			print("Addition result:" + str(a+b+c))
		else:
			# add two numbers
			print("Addition result:" + str(a+b))

s = Sum()
s.add(1,2,3)
s.add(1,2)

#$ python python/polymorphism_overloading.py 
#Addition result:6
#Addition result:3