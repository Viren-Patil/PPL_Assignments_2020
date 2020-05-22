print ("Enter the page numbers between 1 to 25")
page = 0
count = 0
l = [] 
li = range(1,26)
while (count < 25):
	page = int(input("Enter page number(-1 to exit): "))
	
	if page == -1:
		break
	elif page > 25:
		print ("Page number is greater than 25")
	elif page < 0:
		print ("Page number cannot be negative(-1 to exit)")
	else:
		l.append(page)
		count += 1
		
print ("Your list ",set(l))
print ("Missing page numbers: ", list(set(li) - set(l)))
