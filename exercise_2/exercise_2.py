def this_letter_is_equal_to_r(first_letter):
  return True if first_letter.lower() == "r" else False

def are_you_playing_banjo(name):
  first_letter = name[0]

  plays_banjo = " plays banjo"
  doesnt_play_banjo = " does not play banjo"

  return name + plays_banjo if this_letter_is_equal_to_r(first_letter) else name + doesnt_play_banjo
