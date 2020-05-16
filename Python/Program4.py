import random

num = random.choice(range(1, 21))
c = 7

print ("This program has chosen a number between 1 to 20\nYou have 7 chances to guess the number!")

while(c):
	guess = int(input("Guess the number:\t"))
	print (guess)
	if (guess > num):
		print ("Wrong guess!\t HINT: The chosen number is less than %d.\nTry again!"%(guess))
			
	elif (guess < num):
		print ("Wrong guess!\t HINT: The chosen number is greater than %d.\nTry again!"%(guess))
			
	else:
		print ("Congratulations! You guessed it right!!")
		exit(0)
			
	c -= 1
		
choice = str(input("Sorry! You lost all chances\nWant the number to be revealed? Y for YES, any key for NO: "))
if choice == 'Y':
	print (num)



