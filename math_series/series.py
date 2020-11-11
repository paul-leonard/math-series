def fibonacci(n):
  '''With a single input parameter of n, the function calculates and returns the Fibonacci Number.'''
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
  '''With a single input parameter of n, the function calculates and returns the Lucas Number.'''
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas(n-1) + lucas(n-2)

def sum_series(n, first=0, second=1):
  '''This function calculates and returns a sum series such as the Fibonacci Number or Lucas Number.  It can also return a custom number.  If provided with a single argument, the function will find the Fibonacci Number.  Other numbers such as Lucas can be found by entering optional second and third arguments.  For Lucas, enter 2 and 1.  Enter whatever numbers you'd like to discover your very own series!'''
  if n == 0:
    return first
  elif n == 1:
    return second
  else:
    return sum_series(n-1,first,second) + sum_series(n-2,first,second)
