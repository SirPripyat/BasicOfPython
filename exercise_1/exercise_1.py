
def array_diff(a, b):
  return filter_values(a, b)

def filter_values(a, b):
  list = []
  
  for i in a:
    if i not in b:
      list.append(i)

  return list
