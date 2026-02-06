# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
START
  |
  v
Input hot dog type
  |
  v
Set base price
  |
  v
Ask if cheese?
  |----Yes----> Add $0.50
  |
  v
Ask if peppers?
  |----Yes----> Add $0.75
  |
  v
Ask if grilled onions?
  |----Yes----> Add $1.00
  |
  v
Calculate tax (7%)
  |
  v
Calculate total cost
  |
  v
Display cost, tax, total
  |
  v
END

  START PROGRAM

DECLARE basePrice, toppingsCost, tax, totalCost AS REAL
DECLARE choice AS STRING

toppingsCost = 0

DISPLAY "Enter hot dog type (Hot Dog or Chili Dog):"
INPUT choice

IF choice = "Hot Dog" THEN
    basePrice = 3.50
ELSE IF choice = "Chili Dog" THEN
    basePrice = 4.50
END IF

DISPLAY "Add cheese? (yes/no)"
INPUT choice
IF choice = "yes" THEN
    toppingsCost = toppingsCost + 0.50
END IF

DISPLAY "Add peppers? (yes/no)"
INPUT choice
IF choice = "yes" THEN
    toppingsCost = toppingsCost + 0.75
END IF

DISPLAY "Add grilled onions? (yes/no)"
INPUT choice
IF choice = "yes" THEN
    toppingsCost = toppingsCost + 1.00
END IF

tax = (basePrice + toppingsCost) * 0.07
totalCost = basePrice + toppingsCost + tax

DISPLAY "Hot dog cost: $", basePrice + toppingsCost
DISPLAY "Tax: $", tax
DISPLAY "Total cost: $", totalCost

END PROGRAM
