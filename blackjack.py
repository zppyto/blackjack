import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  score = sum(cards)
  if score == 21 and len(cards) == 2:
    return 21
  if 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
    return score
  else:
    return score
  
def compare_score(user_score, computer_score):
  if computer_score > 21:
    print(f"Your final hand: {user_cards}, final score: {user_score}. YOU WON!")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}.")
    return "won"
  elif user_score == 21:
    print(f"Your final hand: {user_cards}, final score: {user_score}. YOU WON!")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}.")
    return "won"
  elif user_score > 21:
    print(f"Your final hand: {user_cards}, final score: {user_score}. YOU LOST!")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}.")
    return "lost"
  elif user_score > computer_score:
    print(f"Your final hand: {user_cards}, final score: {user_score}. YOU WON!")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}.")
    return "won"
  elif user_score < computer_score:
    print(f"Your final hand: {user_cards}, final score: {user_score}. YOU LOST!")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}.")
    return "lost"
  elif user_score == computer_score:
    print(f"Your final hand: {user_cards}, final score: {user_score}. IT'S A DRAW!")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}.")
    return "draw"


exit_game = input("Would you like to play a game of blackjack? Type 'y' or 'n': ")
if exit_game == "y":
  exit_game = False
else:
  exit_game = True
  exit()

user_cards = []
user_cards.append(deal_card())
user_cards.append(deal_card())

computer_cards = []
computer_cards.append(deal_card())
computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

draw_card = input("Type 'y' to get another card, type 'n' to passssss: ")

while draw_card == "y" and exit_game == False:
  user_cards.append(deal_card())
  user_score = calculate_score(user_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card is {computer_cards[0]}")
  results = compare_score(user_score, computer_score)
  if "won" or "lost" in results:
    exit_game = True
  else:
    draw_card = input("Type 'y' to get another card, type 'n' to pazz: ")
    if draw_card == "y":
      compare_score(user_score, computer_score)
      results = compare_score(user_score, computer_score)
    if draw_card == "n":
      draw_card = "n"

while draw_card == "n" and exit_game == False:
  computer_score = calculate_score(computer_cards)
  if computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    compare_score(user_score, computer_score)
    exit_game = True
  elif computer_score > 21:
    compare_score(user_score, computer_score)
    exit_game = True
  else:
    compare_score(user_score, computer_score)
    exit_game = True