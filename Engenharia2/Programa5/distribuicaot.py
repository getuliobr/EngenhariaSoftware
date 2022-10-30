import math

def gamma(x: int) -> float:
  if x == 1:
    return 1
  elif x == 1/2:
    return math.sqrt(math.pi)
  else:
    return (x - 1) * gamma(x - 1)

def distribuicao_t(x: float, dof: float) -> float:
  return gamma((dof + 1) / 2) / (math.sqrt(dof * math.pi) * gamma(dof / 2)) * (1 + x ** 2 / dof) ** (- (dof + 1) / 2)
