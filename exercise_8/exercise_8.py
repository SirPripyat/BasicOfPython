def lovefunc(flower1, flower2):
   
  if number_is_even(flower1) and number_is_odd(flower2):
    return True
  elif number_is_odd(flower1) and number_is_even(flower2):
    return True
  else:
    return False

def number_is_even(number):
  return True if number % 2 == 0 else False

def number_is_odd(number):
  return True if number % 2 != 0 else False