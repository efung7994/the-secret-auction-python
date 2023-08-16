import art
import os

clear = lambda: os.system('clear')

print(art.logo)

auction = True
bidders = []
highest = 0
highest_name = ""

while auction:
  name = input("What is your name? \n")
  bid = input("What is your bid? \n")


  def secret_auction(name, bid):
      bidder = {
          "name" : name,
          "bid" : int(bid)
      }
      bidders.append(bidder)
  secret_auction(name=name, bid=bid)
  add_another = input("Do you want to add another bidder? Y/N \n")
  if add_another.lower() == "n":
    clear()
    auction = False
  else:
    clear()

for bidder in bidders:
  name = bidder["name"]
  bid = bidder["bid"]
  if bid > highest:
    highest = bid
    highest_name = name
  elif bid == highest:
    highest_name = highest_name + ", " + name
print(f"The highest bid made was: {highest}")
print(f"Winner(s): {highest_name}")