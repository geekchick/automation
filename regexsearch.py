# A. Understand the Problem
'''
Write a program that opens all .txt files in a folder
and searches for any line that matches a user-supplied
regular expression. The results should be printed to
the screen.
'''

# B. Manually Solve the Problem
    # 1. Create a list with the different text file names
    # 2. For the first filename in the list, join the filename and the path
    # 3. Open the filename in read mode
    # 4. Read the contents of the File
    # 4a.Search for the regex String
    # 4b.Print out the date
    # 5. Close the File
    # 6. Go to the next filename

# C. Optimize the Manual Solution
    # 1. Create a list with the different text file names
    # 2. For each filename in the list, join the filename and the path
    # 3. Open the filename in read mode
    # 4. Read the contents of the File
    # 5. Search for the Regex String
    # 6. Print out the date
    # 7. Close the file

# D. Pseudocode
    # def readFiles():
        # filenames = ["file1.txt", "file2.txt", "file3.txt"]
        # for item in filenames:
            # fullfile = os.path.join('/Users/tonya/Desktop/ATB/' + item)
            # f = open(fullfile, 'r')
            # filetext = f.read()
            # birthdate = re.compile(r'regex')
            # mo = birthdate.search(filetext)
            # print(mo.group())
            # f.close()

# E. Code
import os
import re

def readFiles():
    filenames = ['regex1.txt','regex3.txt','regex4.txt']
    for file in filenames:
        fullfile = os.path.join('/Users/tonya/Desktop/ATB/' + file)
        #print(fullfile)
        f = open(fullfile, 'r')
        filetext = f.read()
        birthdate = re.compile(r'\d+\/\d\d\/\d\d\d\d')
        mo = birthdate.findall(filetext)
        print(mo)
        f.close()

readFiles()