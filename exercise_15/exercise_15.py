def positive_sum(list):
  filtered_list = filter(remove_negative_numbers, list)

  return sum(filtered_list)

def remove_negative_numbers(number):
  if number < 0: return False
  return True
