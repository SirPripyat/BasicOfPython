def get_grade(s1, s2, s3):
  average = calculate_average(s1, s2, s3)

  return determine_grade(average)

  
def calculate_average(s1, s2, s3):
  return (s1 + s2 + s3) / 3

def determine_grade(average):
  if average >= 90: return "A"
  if average >= 80: return "B"
  if average >= 70: return "C"
  if average >= 60: return "D"
  return "F"