import random

num = random.choice(range(1, 21))
c = 7
n = 1

print ("This program has chosen a number between 1 to 20\nYou have 7 chances to guess the number!")

while(c):
	if (n != 7):
		guess = int(input(f'Guess {n}:\t'))
	else:
		guess = int(input(f'Last Guess:\t'))
		
	if (guess > num):
		print ("\nWrong guess!\t HINT: The chosen number is less than %d.\nTry again!"%(guess))
			
	elif (guess < num):
		print ("\nWrong guess!\t HINT: The chosen number is greater than %d.\nTry again!"%(guess))
			
	else:
		print ("Congratulations! You guessed it right!!")
		exit(0)
			
	c -= 1
	n += 1
		
choice = str(input("Sorry! You lost all chances\nWant the number to be revealed? Y for YES, Enter for NO: "))
if choice == 'Y' or choice == 'y':
	print (num)



