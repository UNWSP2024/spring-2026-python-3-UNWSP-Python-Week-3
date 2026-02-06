# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	                            Price Per Pound
# 2 pounds or less   	                    $1.50
# Over 2 pounds but not more than 6 pounds  $3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	                        $4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    ######################
    START PROGRAM

DECLARE weight, rate, totalCost AS REAL

DISPLAY "Enter the package weight:"
INPUT weight

IF weight <= 2 THEN
    rate = 1.50
ELSE IF weight <= 6 THEN
    rate = 3.00
ELSE IF weight <= 10 THEN
    rate = 4.00
ELSE
    rate = 4.75
END IF

totalCost = weight * rate

DISPLAY "Shipping cost is $", totalCost

END PROGRAM
    ######################
    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
