# KeyboardInterrupt Exception

try:
    inp = input("Press Ctrl+C or Interrupt the Kernel: ")
    
except KeyboardInterrupt:
    print ('\nCaught the KeyboardInterrupt exception\n')

else:
    print ('No exception occurred')


# ZeroDivisionError Exception

p = int(input("Enter dividend: "))
while(1):

    try:
        q = int(input("Enter the divisor: "))
        ans = p / q

    except ZeroDivisionError:
        print("ZeroDivisonError: You tried to divide by 0\nEnter the divisor again!")

    else:
        print("No Exception Occured.")
        print("Result = {}\n".format(ans))
        break


# AssertionError Exception

try:  
    a = 25.25
    b = 'String'
    assert a == b

except AssertionError:  
        print ("AssertionError: AssertionError Exception occurred\n")

else:  
    print ("Success, no error!\n")


# Key Error

try:
    dic = {1:'yay', 2:'hurray', 3:'byee', 4:'see you'}
    print(dic[5])

except LookupError:
    print("LookupError: Key Error occured because the key is not present in the dictionary")

else:
    print("No error while accesing the value of the key.")

# Index Error

try:
    l = [1, 2, 3, 4, 5, 6, 7]
    print(l[9])

except LookupError:
    print("LookupError: Index Error occured because the index went out of bounds.")  

else:
    print("No error while accesing the list.")
    
    
    
  
  
  
  
  
  
  
  
  
  
  
  
  
