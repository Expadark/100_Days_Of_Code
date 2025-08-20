# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from os import system
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidders = {}
more_bidders = True

while more_bidders:
    name = input("What if your name? : ")
    bid = input("How much do you want to bid? :$")
    bidders[name] = int(bid)
    do_again = input("Are there more bidders? Type 'yes' or 'no' : ")
    if do_again == "no":
        more_bidders = False
    system ("cls")

highest_bidder = 0
highest_name = ""

for key in bidders:
    if bidders[key] > highest_bidder:
        highest_bidder = bidders[key]
        highest_name = key

print(f"{highest_name} won at ${highest_bidder}")
input("")