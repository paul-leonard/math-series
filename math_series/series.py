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