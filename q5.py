def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not(type(num) in (float,int) and type(divisor) in (float,int)) :
        print ("input",num,"or/and",divisor,"are not numbers")
        return False  
    elif num % divisor == 0:
        print (num,"is divisible by",divisor,"and return True")      
        return True
    else:
        print (num,"is not divisible by",divisor,"and return False")      
        return False

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

print(check_divisibility(10,2))
print(check_divisibility(7,3))
