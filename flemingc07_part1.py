"""
Author:  Camellia Fleming
Course:  CSC 121
Assignment:  Lesson 07 Lab - Part 1
Description:  Creating Character Names
"""

# get file name from user
fname = input("What is the full name of the file? ")
try:
    #process file
    with open(fname,"r") as fhandle:
        # loop thru the sequence of lines in the file and print each line
        count = 0
        for line in fhandle:
            count = count+1
            clean_line=line.rstrip()
            print(clean_line)
        print('Line Count: ',count)
        # no need to close the file, it is closed automatically using with statement
except:
    print("File cannot be opened. Please check file name.")
