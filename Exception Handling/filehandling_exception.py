while(1):

    file = input("Enter correct filename: ")
    
    try:
    
        filecontent = open(file, 'r')
        content = filecontent.read()

    except IOError:						# Catches the exception for us and let's us execute our own code in case of an exception.
    							
        print("\nFileNotFoundError: File is not found. Please check what you have entered. Try Again!\n")

    else:								# Gets executed if no exceptions occured and everything went smoothly.
    									
        print("Succesfully read the file, '{}'\n".format(file))
        print("File content: {}\n".format(content))
        break
