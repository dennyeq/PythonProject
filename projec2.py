#2 Projec - Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
many_people = int(input("How many people to split the bill? "))
tip_per_person = ((bill * tip / 100) + bill) / many_people
print(f"Each person should pay: ${tip_per_person:.2f}")