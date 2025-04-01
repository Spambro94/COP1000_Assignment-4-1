# This program calculates prices for custom house signs.

# Declare and initialize variables here.
charge = 0.00  # initial charge
numChars = 8   # number of characters on the sign
color = "gold" # color of characters
woodType = "oak"  # type of wood for the sign

# Base charge
charge = 35.00

# Charge for additional characters
if numChars > 5:
    charge += (numChars - 5) * 4

# Charge for oak wood
if woodType == "oak":
    charge += 20.00

# Charge for gold lettering
if color == "gold":
    charge += 15.00

# Output Charge for this sign
print("The charge for this sign is $" + str(charge))