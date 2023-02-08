"""
Author:  Camellia Fleming
Course:  CSC 121
Assignment:  Lesson 07 Lab - Part 2
Description:  Creating Character Names
"""

# get file name from user
fname = input("What is the full name of the file? ")
title = input("Enter a title: ")
try:
    #process file
    with open(fname,"r") as fhandle:
        # loop thru the sequence of lines in the file and print each line
        count = 0
        for line in fhandle:
            if line.startswith(title):
                count = count+1
                line = line.rstrip()
                print(line)
        print(count, 'characters had the title', title)


        # no need to close the file, it is closed automatically using with statement
except:
    print("File cannot be opened. Please check file name.")
