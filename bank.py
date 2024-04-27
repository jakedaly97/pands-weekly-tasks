# bank.py
# Author: Jake Daly
# prompt user and read in two money amounts (in cents),
# add the two amounts, Print out the answer in a human readable format 
# with a euro sign and decimal point between the euro and cent of the amount


print("Welcome to Python Bank") # prints the string "Welcome to python bank"

number1 = int(input("Please enter a number in cents:")) # Prompts user to enter an integer for cents
number2 = int(input("Please enter a 2nd number in cents:")) # Prompts user to enter a second integer for cents

total_cents = number1 + number2 # New variable = number1 + number2
total_euro = total_cents // 100 # Divides the total_cents variable by 100, 100 cents = 1 euro etc.
remaining_cents = total_cents % 100 # Gives the remaining number after total_cent is divided by 100, which will be the remaining cents
balance = total_euro + remaining_cents/100 # Calculates balance by adding total_euro (whole euros) and remaining cents 

print(f"Total balance: €{balance:,}") # Prints out the balance in euro and cents, formatted into a fixed point number with 2 decimal places. String formatting found at W3 schools, https://www.w3schools.com/python/python_string_formatting.asp