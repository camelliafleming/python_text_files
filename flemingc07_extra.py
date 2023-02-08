"""
Author:  Camellia Fleming
Course:  CSC 121
Assignment:  Lesson 07 Lab - Extra Credit
Description:  Creating Character Names
"""

# get file name from user
fname = input("What is the full name of the file? ")
title = input("Enter a title: ")

#def count_title(file):
try:
    #process file
    with open(fname,"r") as fhandle:
        # loop thru the sequence of lines in the file and print each line
        count = 0
        num_chars=0
        for line in fhandle:
            if line.startswith(title):
                line = line.rstrip()
                count = count+1
                num_chars += len(line)
                print(line)
        print(count, 'characters had the title', title)

    # no need to close the file, it is closed automatically using with statement
except:
    print("File cannot be opened. Please check file name.")
    #return(count)

#write number of characters to file
with open('flemingc07_extra_output.txt', 'w') as f:
    f.write((str(num_chars)))

