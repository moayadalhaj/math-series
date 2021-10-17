def fibonacci(n):
    """
    Using recursion to solve fibonacci series
    which takeas an integer number and return it's index 
    in fibonacci series
    """
    if n<=1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

def lucas(n):
    """
    Using recursion to solve Lucas series
    which takeas an integer number and return it's index 
    in fibonacci series
    """
    if n==0:
        return 2
    elif n==1:
        return n
    else:
        return lucas(n-2)+lucas(n-1)

def sum_series(n,a=0,b=1):
    """
    Using recursion to solve sum_series function
    which takeas one requirment integer number and two optional depending on the target series nedded
    then return it's index in that series
    """
    if n==0:
        return a
    if n==1:
        return b
    else:
        return sum_series(n-2,a,b)+sum_series(n-1,a,b)