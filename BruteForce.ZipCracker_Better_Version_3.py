# Import the zipfile and os modules
import zipfile
import os
import time
# List of files within the Passwords folder
passwordfilesList = []
# Create a function that will allow users to set which password file they would like to use

def collectPasswords(file_to_use):
    #Cracking animation loop just to make program look better
    from time import sleep
    cracking = 'CrAcKiNG...'
    for i in range(11):
        print(cracking[i], sep=' ', end=' ', flush=True); sleep(0.5)
    # Create the file path that points to the password dictionary
    filePathtoPasswordDictionary = os.path.join("./Resources/Passwords", file_to_use)
    # Open the file and read it so that it is a string
    wordsFile = open(filePathtoPasswordDictionary)
    wordsText = wordsFile.read()

    # Split the file on newlines so that it is now a list
    splitWordsText = wordsText.split("\n")
    # Return the passwords list
    return splitWordsText
# Create a function that will be used to crack the zip folders
def crackZips(passwords):
    pathtoZips = os.path.join("./Resources/ZippedFiles")
    
    # Loop through all of the zips using the os.walk() function
    for root, dirs, files in os.walk(pathtoZips):
        #print(files, file=f)
        # Loop through each file that is collected
        for oneFile in files:
            #print(oneFile, file=f)
            # Check that the file is a zip file by splitting on the period and checking for zip
            if ".zip" in oneFile:
                # Create the path to the current file
                currentFilePath = os.path.join(pathtoZips, oneFile)
                #print(currentFilePath, file=f)
                # Create a reference to the zipped file
                zipConnection = zipfile.ZipFile(currentFilePath)
                # Loop through each password in the passwords list  
                for password in range(len(passwords)):
                    #print(passwords[password], file=f)
                    # Try to extract all of the files in the zipped file using the current password
                    try:
                        zipConnection.extractall(pwd=passwords[password].encode())

                        # Print out what the password for the zipped file was
                        #print("PASSWORD: " + passwords[password], file=f)
                        print("Success! Password Found." + "\n" + "Password: " + passwords[password] + "   Location: " + oneFile + "\n")

                    # If the file fails to open with the current password, move onto the next one
                    except:
                        pass
# Loop through the file names for the password files
tempdirlist = []
tempdirlist = os.listdir("./Resources/Passwords")
#print(tempdirlist)
for onefile in tempdirlist:
    if ".txt" in onefile:
        passwordfilesList.append(onefile)
        #print(passwordfilesList)

# Print a header statement to give the user a simple set of operations to navigate
print("""    
_|_|_|_|_|  _|_|_|  _|_|_|          _|_|_|  _|_|_|      _|_|      _|_|_|  _|    _|  _|_|_|_|  _|_|_|    
      _|      _|    _|    _|      _|        _|    _|  _|    _|  _|        _|  _|    _|        _|    _|  
    _|        _|    _|_|_|        _|        _|_|_|    _|_|_|_|  _|        _|_|      _|_|_|    _|_|_|    
  _|          _|    _|            _|        _|    _|  _|    _|  _|        _|  _|    _|        _|    _|  
_|_|_|_|_|  _|_|_|  _|              _|_|_|  _|    _|  _|    _|    _|_|_|  _|    _|  _|_|_|_|  _|    _|  
""")
print("This program will crack your zip" + "\n")
print("Please choose from list below:" + "\n")
userimput = input(str(passwordfilesList) + ": ")
passwordlist = collectPasswords(userimput)

with open("output.txt", "w") as f:  
    crackZips(passwordlist)
# Ask the user if they would like to crack another
while True:
    answer = input("More Cracking? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        print("Please choose from list below:" + "\n")
        userimput = input(str(passwordfilesList) + ": ")
        passwordlist = collectPasswords(userimput)

        with open("output.txt", "w") as f:  
            crackZips(passwordlist)
            
        print("\n")
    else:
        print("Done Cracking. Goodbye" + "\n")
        break