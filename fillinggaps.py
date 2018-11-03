
# A. Understand the problem
'''
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
and so on, in a single folder and locates any gaps in the numbering (such as if there is a
spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files
to close this gap.
'''

# B. Manually solve the Problem
    # 1. Get all the files in a directory
    # 2. For each item in the directory, check if the item starts with spam, like spam001.txt
    # 3. If the item starts with spam then find the '.'
    # 3b. put everything from the beginning of the string to the end of the period into a new varaible
    # 4. Loop through the new string, spam001
    # 5. Check if each character is in numbers 1 - 9
    # 6. If it is in the list then add to create_number
    # 7. Else, if the character is not in list then continue
    # 8. Start var at 0
    # 9. If new_number + 1 is equal to var then increment var by 1 and continue
    #10. Else, if new_number is not equal to var then print out each file name and it's replacement


# D. Pseudocode
# text_list = ['spam001.txt','spam002.txt', 'spam003txt'] # , spam002.txt, spam003txt
#
# def locateGaps():
#     new_word_prefix = ''
#     numbers_list = ['1','2','3','4','5','6','7','8','9']
#
#     var = 0

#     for file in text_list:
#         create_number = ''
#         if file.startswith('spam'):
#             period_pointer = file.find('.')
#             new_word_prefix = file[0:period_pointer]
#             #print(new_word_prefix)
#
#         for character in new_word_prefix:
#             if character in numbers_list:
#                 create_number += character
#                     #print("This is the new string: ", create_number)
#             else:
#                 continue
#
#
#             new_number = int(create_number)
#             if var == new_number + 1:
#                 var += 1
#                 continue
#
#



# E. Code


# A. Understand the problem
'''
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
and so on, in a single folder and locates any gaps in the numbering (such as if there is a
spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files
to close this gap.
'''

text_list = ['spam001.txt', 'spam003.txt', 'spam005.txt',
             'spam006.txt']  # , spam002.txt, spam003txt


def locateGaps():
    old_list = ['spam001.txt', 'spam003.txt', 'spam005.txt', 'spam006.txt']  # , spam002.txt, spam003txt

    import os

    new_list = []
    for i in range(0, len(old_list)):
        new_list.append('spam' + str(i + 1).rjust(3, '0') + '.txt')

    print(new_list)

    for i in range(len(new_list)):
        os.rename(old_list[i], new_list[i])

'''
#import os

old_list = ['spam001.txt','spam003.txt', 'spam005.txt', 'spam006.txt'] # , spam002.txt, spam003txt
new_list = ['spam' + str(i+1).rjust(3, '0') + '.txt' for i in range(0, len(old_list))]

print(new_list)
   
for i in range(len(new_list)):
    os.rename(old_list[i], new_list[i])
'''

print(locateGaps())

