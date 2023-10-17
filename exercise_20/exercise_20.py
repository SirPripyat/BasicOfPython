def xo(string):

  count_x = 0
  count_o = 0

  for letter in string:
    if letter.lower() == "x":
      count_x += 1
    elif letter.lower() == "o":
      count_o += 1
    
  return True if count_x == count_o else False
