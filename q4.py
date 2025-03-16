def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    print ("The string is",s)
    print ("After reversing... ")
    r =""
    for x in range(len(s)-1, -1, -1):
        r += s[x]
        print("Character at index ", x ,":",s[x])
    print ("The reverse string is",r)
    return r



# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
s1 = "Hello World"
string_reverse(s1)
s2 = "Python"
string_reverse(s2)
