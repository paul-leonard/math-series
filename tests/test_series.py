from math_series.series import fibonacci
from math_series.series import lucas

######## Tests for fibonacci function ########
def test_fibonacci_0():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_1():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_2():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fibonacci_3():
  actual = fibonacci(3)
  expected = 2
  assert actual == expected

def test_fibonacci_4():
  actual = fibonacci(4)
  expected = 3
  assert actual == expected

def test_fibonacci_9():
  actual = fibonacci(9)
  expected = 34
  assert actual == expected

def test_fibonacci_12():
  actual = fibonacci(12)
  expected = 144
  assert actual == expected


######## Tests for lucas function ########
def test_lucas_0():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_1():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_2():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lucas_3():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test_lucas_4():
  actual = lucas(4)
  expected = 7
  assert actual == expected

def test_lucas_9():
  actual = lucas(9)
  expected = 76
  assert actual == expected

def test_lucas_10():
  actual = lucas(10)
  expected = 123
  assert actual == expected
