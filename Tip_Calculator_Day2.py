print("Hiii, Welcome to the Tip Calculator")
bill = float(input("What's the total Bill ? $"))
tip = int(input("Enter the tip you would like to pay 10 12 or 15 :"))
people = int(input("Among how many people would you like to divide the bill ?"))
total = ((tip / 100) * bill + bill)
f_total = total / people #f_total is the final bill after dividing it among the number of people
r_total = round(f_total, 2) #r_total is the round off of the total bill
print("Each person should pay: $", r_total)
