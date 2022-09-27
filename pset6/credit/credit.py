from math import floor


def main():
  card = get_int("Number: ")
  if card < 1000000000000:
    print("INVALID")
    exit(0)

  [first, summed] = resolve_card(card)
  print_result(first, summed)


def get_int(arg: str = "") -> int:
  while True:
    try:
      return int(input(arg))
    except:
      continue


def resolve_card(card: int):
  first = 0
  summed = 0
  index = 0
  while card:
    digit = card % 10
    if card > 9:
      first = card
    if index % 2 == 1:
      digit *= 2
    index += 1
    summed += floor(digit / 10)
    summed += floor(digit % 10)
    card = floor(card / 10)
  return [first, summed]


def print_result(first, summed):
  if summed % 10 != 0:
    print("INVALID")
  elif first == 34 or first == 37:
    print("AMEX")
  elif round(first / 10) == 4:
    print("VISA")
  elif first >= 51 and first <= 55:
    print("MASTERCARD")
  else:
    print("INVALID")


main()
