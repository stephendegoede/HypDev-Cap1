# The following code calculates either an investment
# or a bond repayment.

# Import the necassary libraries.
import math

# Print the initial information about the calculator.
print("Welcome to the financial calculator.")
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment\t- to calculate the amount of interest you'll earn on investment")
print("bond\t\t- to calculate the amount you'll have to pay on a home loan")

# Request the user to input the type of calculation and transform it to lowercase.
calc = input("\nEnter investment or bond - type investment/bond: ").lower()
print(calc)

# Determine which type was entered and if it was entered correctly.
# If investment was chosen, request the user to input the
# variables required to calculate the investment.
if calc == "investment":
    deposit = float(input("\nPlease enter the amount of money that you are depositing: "))

    rate = float(input("Please enter the interest rate as a percentage: "))

    n = float(input("Please enter the number of years you plan to invest: "))

    interest = input("Please enter if you want simple or compound interest - type simple/compound: ").lower()

# Calculate the investment based on the users inputs
# and print the answer to screen. The answer is rounded to two digits.
    if interest == "simple":
        answer = round((deposit * (1 + rate/100 * n)), 2)

        print(f"\nYour investment will be worth R{answer} after {n} years.")

    elif interest == "compound":
        answer = round((deposit * math.pow((1 + rate/100), n)), 2)

        print(f"\nYour investment will be worth R{answer} after {n} years.")

    else:
        print("\nYou have not selected the type of interest correctly.\nPlease run and try again.")

# If bond was chosen, request the user to input the
# variables required to calculate the monthly repayments.
elif calc == "bond":
    present_value = float(input("\nPlease enter the present value of the house: "))

    rate = float(input("Please enter the annual interest rate as a percentage: "))

    n = float(input("Please enter the number of months you plan to repay: "))

# Calculate the bond repayment based on the users inputs
# and print the answer to screen. The answer is rounded to 2 digits.
    answer = round(((rate / 12 / 100 * present_value) / (1 - math.pow((1 + rate / 12 / 100), -n))), 2)

    print(f"\nYour monthly bond repayment will be R{answer}.")

# If the user entered the type of calculation incorrectly,
# print the fact to screen.
else:
    print("\nYou have not entered the type of calculation correctly.\nPlease run and try again.")