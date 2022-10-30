from distribuicaot import distribuicao_t
from simpson import simpson
import math

def test1():
  res = simpson(distribuicao_t, 10, 0.00001, 1.1, 9)
  assert math.fabs(res - 0.3500589) < 0.0001

def test2():
  res = simpson(distribuicao_t, 10, 0.00001, 1.1812, 10)
  assert math.fabs(res - 0.36757) < 0.0001


def test3():
  res = simpson(distribuicao_t, 10, 0.00001, 2.750, 30)
  assert math.fabs(res - 0.49500) < 0.0001