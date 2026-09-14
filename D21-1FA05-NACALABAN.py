import math

# --- Program Start ---

# Get user input for the coordinates of the two points
# Using float() allows for decimal inputs, making the program more versatile
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Calculate the distance using the Euclidean distance formula
    # math.pow(base, exp) raises the base to the power of exp
    # math.sqrt(x) returns the square root of x
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    # Display the result clearly
    # Formatting to 2 decimal places for readability, though full precision is available
    print(f"The distance between the two points is: {distance:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for the coordinates.")

# --- Reflection ---
# Using a library like 'math' is more practical than writing calculations from scratch 
# because it provides optimized, pre-tested functions like sqrt() and pow() that ensure 
# accuracy and save development time. Without these library functions, we would need 
# to implement complex algorithms for square roots and exponents manually, increasing 
# the risk of errors and making the code harder to read and maintain.

#--- What did you change and why? ---
# I further improved the README.md file and gave examples using the formula.
# I changed the README.md file and improved to show effectivity of the Euclidean Distance Formula.
