def calculate_average(list_of_numbers, list_of_numbers_2):
  average_1 = average(list_of_numbers)

  average_2 = average(list_of_numbers_2)

  total_average = average([average_1, average_2])

  return {
    'A': average_1,
    'B': average_2,
    'C': total_average
  }
  

def average(numbers):
  return sum(numbers) / len(numbers)

print(calculate_average([10, 10, 10], [10, 10, 10])) 