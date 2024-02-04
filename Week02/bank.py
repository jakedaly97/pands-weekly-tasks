#bank.py
#Weekly task 02, prompt user and read in two money amounts (in cents),
#add the two amounts, Print out the answer in a human readable format 
#with a euro sign and decimal point between the euro and cent of the amount
#Author: Jake Daly

print("Welcome to Python Bank")
number1 = int(input("Please enter a number in cents:"))
number2 = int(input("Please enter a 2nd number in cents:"))
total_cents = number1 + number2
total_euro = total_cents // 100
remaining_cents = total_cents % 100
print("Total balance: €{:.2f}".format(total_euro + remaining_cents/100))