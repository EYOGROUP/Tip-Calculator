print("Welcome to the tip calculator,")

total_bill = input("What was the total bill? \n")

split_bill = input("How many people to split the bill?  \n ")

pourcentage = input("what percentage tip would you like to give? 10, 12, or 15? \n")

split = float(total_bill) /float (split_bill)
pay = split + (split * (float(pourcentage) / 100 ))


print("Each person should pay: €", round(pay, 2))