print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
n_tip = (tip * 0.01) + 1
print(f"Each person should pay ${round(((bill * n_tip)/people), 2)}")
