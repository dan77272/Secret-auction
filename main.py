from replit import clear

print('''   ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
      ''')

bidders = {}
print("\n\nWelcome to the secret auction program")


def game():
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bidders[name] = bid


while True:
    game()
    choice = input("\nAre there any other bidders? Type 'yes' or 'no': ")
    if choice == "yes":
        clear()
        continue
    elif choice == "no":
        break
highestBid = 0
for bidder in range(0, len(bidders)):
    if int(list(bidders.values())[bidder]) > highestBid:
        highestBid = int(list(bidders.values())[bidder])

key_list = list(bidders.keys())

value_list = list(bidders.values())

position = value_list.index(str(highestBid))
print(f"The winner is {key_list[position]} with a bid of ${highestBid}")
