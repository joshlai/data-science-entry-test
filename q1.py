def swap(x, y):

    # Task 1
    # Create a function that would swap the value of x and y using only x and y as variables.
    # x and y must be numeric.
    # Return -1 if x and y is not numeric, and
    # print the swapped values if both x and y are numeric.

    if not(type(x) in (float,int) and type(y) in (float,int)) :
        return -1  
    else:
        x, y = y, x
        print(f"Swapped values: x = {x}, y = {y}")

    return 

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# Scenario #1 returns -1, but this is not printed because the returned value is not handled (e.g., via print(swap("Apple", 10)).
swap("Apple", 10)

# Scenario #2 prints the swapped values and returns None.
swap(9, 17)
    
