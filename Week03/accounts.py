# accounts.py
# Author: Jake Daly
# program that reads in a 10 character account number,
# outputs the account number with only the last 4 digits showing,
# The first 6 digits replaced are replaced with Xs

account_number = str(input("Please enter your 10 digit account number:"))
censor = "XXXXXX"

print(censor + account_number[6:])

# I used W3schools python slicing tutorial to help me with this
# https://www.w3schools.com/python/python_strings_slicing.asp
# I have the program prompt the user to enter their 10 digit number,
# this is inputted as a string type variable
# I created a second string type variable called censor
# censor is just 6 "X" characters in a row
# I then have the program print the censor variable + the account_number variable
# The account_number is sliced, only index 7 to 10 are present which are the last 4 digits in the variable