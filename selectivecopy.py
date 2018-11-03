'''
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.
'''

import os, shutil

def findFiles():
    path = '/Users/tonya/Desktop/C'
    os.chdir('/Users/tonya/Desktop/C')

    for folderName, subfolders, filenames in os.walk('/Users/tonya/Desktop/C'):
        #print("The current folder is " + folderName)

        #for subfolder in subfolders:
            #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

        for filename in filenames:
            #print('FILE INSIDE ' + folderName + ': ' + filename)
            if filename.endswith('.txt'):
                #filepath = os.path.basename(filename)
                print('FILE INSIDE ' + folderName + ': ' + filename)
                folderFilePath = os.getcwd()
                print('Folder File Path ' + folderFilePath)
                #print('This is the Base Name: ' + filepath )
                #print("This is a text file!")
                os.chdir('/Users/tonya/Desktop/C')
                filepath = folderName + '/' + filename
                print("This is the filepath: " + filepath)
                shutil.copy(filepath, '/Users/tonya/Documents/ATB-copy')

findFiles()