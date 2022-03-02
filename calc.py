print("Tip Calc!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,20 or 15?"))
people =int(input("How many people to split the bill? "))
Total_amount = tip/100*bill+bill
Amount_per_person = Total_amount/2
print(f"Each person have to pay: ${Amount_per_person}" )
