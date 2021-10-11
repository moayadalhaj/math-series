def fibonacci(n):
    """
    Using recursion to solve fibonacci series
    """
    if n<=1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

def lucas(n):
    """
    Using recursion to solve Lucas series
    """
    if n==0:
        return 2
    elif n==1:
        return n
    else:
        return lucas(n-2)+lucas(n-1)