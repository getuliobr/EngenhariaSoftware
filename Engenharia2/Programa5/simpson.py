import math

def simpson(F, num_seg: int, E: float, x: float, dof: int) -> float:
  p = 0
  prevsP = math.inf
  while math.fabs(p - prevsP) > E:
    prevsP = p
    W = x / num_seg
    p = F(0, dof) + F(x, dof)
    for i in range(1, num_seg):
      p += 2 * F(i * W, dof) if i % 2 == 0 else 4 * F(i * W, dof)
    p *= W / 3
    num_seg *= 2
  return p