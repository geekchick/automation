# A. Understand the Problem
'''
Write a program that walks through a folder tree and searches for large files
or folders. Print the files with their absolute path and file size to the screen.
'''

# B. Manually Solve the Problem
    # 1. Walk through the folder tree
    # 2.



# C. Pseudocode
    # def findSize():
        # os.chdir('/Users/tonya/Desktop/C')
        # for folderName, subfolders, filenames in os.walk('/Users/tonya/Desktop/C'):
            # print("The FOLDERNAME: " + folderName + " is size: " + os.path.getsize(folderName) + " and the path is: " + os.path.abspath(folderName))

            #for subfolder in subfolders:
                #print("The SUBFOLDERNAME: " + subfolder + " is size: " + os.path.getsize(subfolder) + " and the path is: " + os.path.abspath(subfolder))

                # for file in filenames:
                    # print("The FILENAME: " + file + " is size: " + os.path.getsize(file) + " and the path is: " + os.path.abspath(file))


# D. Code
import os
def findSize():
    os.chdir('/Users/tonya/Desktop/C')
    for folderName, subfolders, filenames in os.walk('/Users/tonya/Desktop/C'):
        print("The FOLDERNAME: " + folderName + " is size: " + str(os.path.getsize(folderName)) + " and the path is: " + os.path.abspath(folderName))

        for subfolder in subfolders:
            print("The SUBFOLDERNAME: " + subfolder + " is size: " + str(os.path.getsize(subfolder)) + " and the path is: " + os.path.abspath(subfolder))

            for file in filenames:
                print("The FILENAME: " + file + " is size: " + str(os.path.getsize(file)) + " and the path is: " + os.path.abspath(file))

findSize()