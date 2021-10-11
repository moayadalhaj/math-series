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

def sum_series(n,a=0,b=1):
    if n==0:
        return a
    if n==1:
        return b
    else:
        return sum_series(n-2,a,b)+sum_series(n-1,a,b)