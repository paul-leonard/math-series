from math_series.series import fibonacci

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
