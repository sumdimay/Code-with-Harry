def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
    
    
    
number = int(input('Enter number: '))
fibonacci(number)
