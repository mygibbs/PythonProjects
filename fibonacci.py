def fibonacci(n):
    n = n + fibonacci(n)
    print n
    return n
    
fibonacci(1)