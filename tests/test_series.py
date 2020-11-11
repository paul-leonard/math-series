from math_series.series import fibonacci
from math_series.series import lucas
#from math_series.series import sum_series


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


######## Tests for sum_series function ########
######## for fibonacci w single argument ########
def test_sum_series_0():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test_sum_series_1():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test_sum_series_2():
  actual = sum_series(2)
  expected = 1
  assert actual == expected

def test_sum_series_3():
  actual = sum_series(3)
  expected = 2
  assert actual == expected

def test_sum_series_4():
  actual = sum_series(4)
  expected = 3
  assert actual == expected

def test_sum_series_9():
  actual = sum_series(9)
  expected = 34
  assert actual == expected

def test_sum_series_12():
  actual = sum_series(12)
  expected = 144
  assert actual == expected

######## Tests for sum_series function ########
######## for fibonacci w 3 arguments ########
def test_sum_series_0():
  actual = sum_series(0,0,1)
  expected = 0
  assert actual == expected

def test_sum_series_1():
  actual = sum_series(1,0,1)
  expected = 1
  assert actual == expected

def test_sum_series_2():
  actual = sum_series(2,0,1)
  expected = 1
  assert actual == expected

def test_sum_series_3():
  actual = sum_series(3,0,1)
  expected = 2
  assert actual == expected

def test_sum_series_4():
  actual = sum_series(4,0,1)
  expected = 3
  assert actual == expected

def test_sum_series_9():
  actual = sum_series(9,0,1)
  expected = 34
  assert actual == expected

def test_sum_series_12():
  actual = sum_series(12,0,1)
  expected = 144
  assert actual == expected


######## Tests for sum_series function ########
######## for lucas w 3 arguments ########
def test_sum_series_0():
  actual = sum_series(0,2,1)
  expected = 2
  assert actual == expected

def test_sum_series_1():
  actual = sum_series(1,2,1)
  expected = 1
  assert actual == expected

def test_sum_series_2():
  actual = sum_series(2,2,1)
  expected = 3
  assert actual == expected

def test_sum_series_3():
  actual = sum_series(3,2,1)
  expected = 4
  assert actual == expected

def test_sum_series_4():
  actual = sum_series(4,2,1)
  expected = 7
  assert actual == expected

def test_sum_series_9():
  actual = sum_series(9,2,1)
  expected = 76
  assert actual == expected

def test_sum_series_10():
  actual = sum_series(10,2,1)
  expected = 123
  assert actual == expected

######## Tests for sum_series function ########
######## for random 3 arguments ########

def test_sum_series_10():
  actual = sum_series(3,3,3)
  expected != None
  assert actual == expected