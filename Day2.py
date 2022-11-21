#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")

percentage = input("What percentage tip would you like to give? 10,12, or 15?")

people = input("How many people to split the bill?")

pay = float(bill) * ((float(percentage))/100 + 1) / int(people)

final_pay = round(pay,2)

print(f"Each person should pay: ${final_pay}")
