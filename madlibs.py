# A. Understand the problem

'''
Create a MadLibs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB or VERB
appears in the text file. For example, a text file may look like this:

    The ADJECTIVE panda walked to the NOUN1 and then VERB. A nearby NOUN2
    was unaffective by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
> silly
Enter a noun:
> chandelier
Enter a verb:
> screamed
Enter a noun:
> pickup truck

The following text file would then be created:
    The silly panda walked to the chandelier and then screamed. A nearby pickup
    truck was unaffected by these events.
'''

# B. Manually Solve the Problem
    #1. Create alist with [ADJECTIVE, NOUN, VERB, NOUN]
    #2. Enter the adjective: silly, append to wordslist
    #3. Enter the noun: chandelier, append to wordslist
    #4. Enter the verb: screamed, append to wordslist
    #5. Enter the noun: truck, append to wordslist
    #6. Read in the file
    #7. For item 'silly' in wordslist, replace file with the first word in alist, increment the counter by 1
    #8. For item 'chandelier' in wordslist, replace file with second word in alist, increment the counter by 1
    #9. For item 'screamed' in wordslist, replace file with third word in alist, increment the counter by 1
    #10.For item 'truck' in wordslist, replace file with fourth word in alist, increment the counter by 1
    #11.Write out the file

# C. Optimize the Manual Problem
    #1. Create alist with [ADJECTIVE, NOUN, VERB, NOUN]
    #2. Enter each part of speech to input and append to wordslist
    #3. Read in the file
    #4. For each item in wordslist replace the item in alist by the item in wordslist, increment counter by 1
    #5. Write out the file

# D. Pseudocode
    # def madlib(paragraph):
        # count = 0
        # alist = [ADJECTIVE, NOUN, VERB, NOUN]
        # wordslist = []
        # adj = input("Enter the adjective: )
        # wordslist.append(adj)
        # noun = input("Enter the noun: )
        # wordslist.append(noun)
        # verb = input("Enter the verb:" )
        # wordslist.append(verb)
        # noun2 = input("Enter the noun:")

        # wordslist.append(noun2)

        # f = open('/Users/tonya/Desktop/ATB/words.txt', 'r')
        # fileData = f.read()
        # f.close()


        # newdata = ""
        #i = 0

        # for item in wordslist:
            # newdata = fileData.replace('alist[i]','item')

        # f = open('/Users/tonya/Desktop/ATB/words.txt', 'w')
        # f.write(newdata)
        # f.close()

        # f.open('/Users/tonya/Desktop/ATB/words.txt', 'r')
        # f.read()

# Code

def madlib():

        # file = open('/Users/tonya/Desktop/ATB/words.txt', 'r')
        # filedata = file.read()
        # print(filedata)

        alist = ['ADJECTIVE', 'NOUN1', 'VERB', 'NOUN2']
        wordslist = []

        adj = input("Enter the adjective: ")
        wordslist.append(adj)
        noun = input("Enter the noun:" )
        wordslist.append(noun)
        verb = input("Enter the verb:" )
        wordslist.append(verb)
        noun2 = input("Enter the noun:")
        wordslist.append(noun2)

        print(wordslist)

        f = open('/Users/tonya/Desktop/ATB/words.txt')
        filedata = f.read()
        print(filedata)
        f.close()

        i = 0

        f = open('/Users/tonya/Desktop/ATB/words.txt', 'w')
        for item in wordslist:
            print("This is filedata = ", filedata)
            print("This is alist[i] = ", alist[i])
            print("This is item = ",item)

            filedata = filedata.replace(alist[i],item)

            i += 1

        f.write(filedata)
        f.close()

        f = open('/Users/tonya/Desktop/ATB/words.txt', 'r')
        print(f.read())

madlib()