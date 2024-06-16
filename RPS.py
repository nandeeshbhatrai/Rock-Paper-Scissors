# DEFINING GLOBAL VARIABLES
moves = {}  # moves dictionary


def player(prev_play, opponent_history=[], ai_history=[], n=3):
  opponent_history.append(prev_play)  # Opponent history
  guess = "R"

  if len(opponent_history) > n:
    sequence = "".join(opponent_history[-n:])
    possible_moves = [sequence + "R", sequence + "P", sequence + "S"]

    if "".join(opponent_history[-(n + 1):]) not in moves.keys():
      moves["".join(opponent_history[-(n + 1):])] = 1
    else:
      moves["".join(opponent_history[-(n + 1):])] += 1

    for i in possible_moves:
      if i not in moves.keys():
        moves[i] = 0

    prediction = max(possible_moves, key=lambda key: moves[key])

    if prediction[-1] == "R":
      guess = "P"
    if prediction[-1] == "P":
      guess = "S"
    if prediction[-1] == "S":
      guess = "R"

  return guess
