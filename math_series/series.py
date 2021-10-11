def fibonacci(n):
    """
    Using recursion to solve fibonacci series
    """
    if n<=1:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)
