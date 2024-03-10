# es.py
# Author: Jake Daly
# Program that reads in a text file and outputs the number of e's it contains,
# Program takes the filename from an argument on the command line.


import sys # Module is used to access command line arguments

my_text_file = sys.argv[1] # sys.argv[1] is the text file name in the command line argument, sys.argv[0] is the name of the program i.e es.py

with open (my_text_file, "r") as f: # opens the file in read mode

    f_cont = f.read() # reads the content of the file

    e_count = f_cont.lower().count("e") # converts the texts in the file to lowercase and then counts the occurance of the letter "e"


print(e_count) # prints out how many times "e" was counted.

# Assumptions
# This program assumes file name will be provided.
# Program assumes the file exists.
# Program assumes file is only text and does not count the letter e if it is an image etc.

# Resources
# https://www.youtube.com/watch?v=ZQ9JO0e9468 shows how to take the filename from an arguemtnt in the command line.
# https://learnpython.com/blog/python-string-methods/ counting strings in python

