def points(games):
  gained_points = 0
  for home_score, nothing, away_score in games:
    if home_score > away_score:
      gained_points += 3
    elif home_score == away_score:
      gained_points += 1
  return gained_points