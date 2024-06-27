def factorial_num(num):
    """This function calculates the factorial of a number using recursion.
    
    Args:
        num (int): This is the number to find the factorial for

    Returns:
        int or str: The factorial of the number, or an error message if the input is invalid
    """
    if isinstance(num, int):
        if num < 0:
            return "Enter a positive integer"
        elif num == 0:
            return 1
        else:
            return num * factorial_num(num - 1)
    else:
        return "Enter a valid integer"

#testing
print(factorial_num("me")) #Output:Enter a valid integer
print(factorial_num(-5)) #Output:Enter a positive integer
print(factorial_num(3)) #Output:6


