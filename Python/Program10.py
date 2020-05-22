
print ("Enter the first number and the common ratio")
a = int(input("First number: "))
r = float(input("Common ratio: "))
c = 0
l = []
print ("The first 10 numbers of GS are:")
while c < 10:
	l.append(a * (r**c))
	c += 1
print (l)	
