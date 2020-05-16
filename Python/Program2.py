import random
while(1):
	print ("The dice shows number: ",random.choice(range(1, 7)))
	choice = str(input("If you want to roll dice again, press Y(y) else press N(n):\t"))
	if choice == 'Y' or choice == 'y':
		continue
	elif choice == 'N' or choice == 'n':
		break
	else:
		print ("Invalid choice!")
		break
