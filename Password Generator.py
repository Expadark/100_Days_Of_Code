import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passlist = []
for char in range(0 , nr_letters):
    char1 = random.choice(letters)
    passlist.append(char1)

for sym in range(0 , nr_symbols):
    sym1 = random.choice(symbols)
    passlist.append(sym1)

for numb in range(0 , nr_numbers):
    num1 = random.choice(numbers)
    passlist.append(num1)

password = ""
random.shuffle(passlist)
for pw in passlist:
    password += pw
print(f"Your password is : {password}")
input("")