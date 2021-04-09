from replit import clear 
from art import logo

# Function to compute the highest bidder
def highest_bidder(bid_record):
    winner = ""
    max_bid = 0
    for name in bid_record:
        if bid_record[name] > max_bid:
            winner = name
            max_bid = bids[name]
    
    print(f"The winner is {winner} with a bid of £{max_bid}.")

print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_continues = True

while bidding_continues:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: £"))

    bids[name] = price

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    clear()
    if another_bidder == "no":
        bidding_continues = False
        highest_bidder(bids)    
