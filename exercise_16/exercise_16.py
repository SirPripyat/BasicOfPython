
def generate_hashtag(string):
  string_size = len(string)

  if string_size > 139 or string_size == 0: 
    return False

  handled_string = remove_white_spaces_and_split_it(string)

  hashtag = "#" + change_to_uppercase(handled_string)

  return hashtag

def remove_white_spaces_and_split_it(string):
  return string.strip().split(" ")

def change_to_uppercase(list_of_string):
  new_string = "" 

  for string in list_of_string:
    if(string == ""): continue
    new_string += string[0].upper() + string[1:].lower()

  return new_string

print(generate_hashtag("ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq"))