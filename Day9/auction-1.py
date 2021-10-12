from art import logo

print(logo)


bids = {}
bid_finishid = True


def highest_bid(bidding):
    highest = 0
    winner = ''
    for key in bids:
        bid_amount = bids[key]
        if bid_amount > highest:
            highest = bid_amount
            winner = key
    print(f"The winner is {winner} with the bid of ${bid}")


bid_finishid = False
while not bid_finishid:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    repeat = input("Are they any other bidders? Type 'yes' or 'no'\n ")
    if repeat == "no":
        bid_finishid = True
        highest_bid(bids)
