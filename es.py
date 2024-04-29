# es.py
# Author: Jake Daly
# Program that reads in a text file and outputs the number of e's it contains,
# Program takes the filename from an argument on the command line.
# Program gives an error if filename is not found in the command line or if the filename does not end in .txt.


import sys # module is used to access command line arguments
import os # module used to allow python to interact with the operating system
import os.path # submodule of os, gives access to isfile() funtion

if len(sys.argv) != 2: # checks if the length of the sys.argv is not equal to 2. sys.argv should be equal to 2 if the .txt file is provided, as there will be 2 elements in the command line.
    print("Error, file name not entered.") # prints out error message 
else:
    my_text_file = sys.argv[1] # sys.argv[1] is the text file name in the command line argument, sys.argv[0] is the name of the program i.e es.py
    if os.path.isfile(my_text_file) == False: # os.path.isfile() checks if my_text_file exists and outputs a boolean value of "True" if it does or "False" if it dosnt
        print("Error, file not detected.") # prints an error if value is false
    if not my_text_file.endswith(".txt"): # checks if the variable ends with ".txt"
        print("Error, .txt file not detected.") # if it dosnt it gives an error
    else:
        with open (my_text_file, "r") as f: # opens the file in read mode
            f_cont = f.read() # reads the content of the file
            e_count = f_cont.lower().count("e") # converts the texts in the file to lowercase and then counts the occurance of the letter "e"
            print(e_count) # prints out how many times "e" was counted.

# Assumptions
# This program assumes file name will be provided.
# Program assumes the file exists.
# Program assumes file is only text and does not count the letter e if it is an image etc.

# Resources
# https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/ tutorial on how to use python to check if a file exists
# https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/ command line arguments and sys.argv
# https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file Shows how to check the extension of a file with .endswith()
# https://www.youtube.com/watch?v=ZQ9JO0e9468 shows how to take the filename from an arguemtnt in the command line.
# https://learnpython.com/blog/python-string-methods/ counting strings in python