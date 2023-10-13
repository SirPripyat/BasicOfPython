def is_triangle(a, b, c):

  absolute_difference = abs(b - c)

  side_sum = b + c

  if absolute_difference < a < side_sum:
    return True
  return False

