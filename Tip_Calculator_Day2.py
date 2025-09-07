print("Hiii, Welcome to the Tip Calculator")
bill = float(input("What's the total Bill ? $"))
tip = int(input("Enter the tip you would like to pay 10 12 or 15 :"))
people = int(input("Among how many people would you like to divide the bill ?"))
total = ((tip / 100) * bill + bill)
f_total = total / people
ff_total = round(f_total, 2)
print("Each person should pay: $", ff_total)