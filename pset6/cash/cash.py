def main():
  cash = get_positive_float("Change owed: $")
  coins = get_coins(cash)
  print(coins)
  pass


def get_float(arg: str = "") -> float:
  while True:
    try:
      return float(input(arg))
    except:
      continue


def get_positive_float(arg: str = "", max: float = None) -> float:
  while True:
    x: float = get_float(arg)
    if max and x > max:
      continue
    if x > 0:
      return x


def get_coins(cash: float) -> int:
  cash = cash * 100
  coins: int = 0
  while cash >= 25:
    cash -= 25
    coins += 1
  while cash >= 10:
    cash -= 10
    coins += 1
  while cash >= 5:
    cash -= 5
    coins += 1
  while cash >= 1:
    cash -= 1
    coins += 1
  return coins


main()
