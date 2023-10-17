def disemvowel(string_):
  vowels = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]

  for letter in string_:
    if letter in vowels:
      string_ = string_.replace(letter, '')

  return string_

