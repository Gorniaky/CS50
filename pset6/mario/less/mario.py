def main():
  height = get_positive_int("Height: ", 8)
  print_pyramid(height)


def get_int(arg: str) -> int:
  while True:
    try:
      x = int(input(arg))
      break
    except:
      continue
  return x


def get_positive_int(arg: str, max: int = None) -> int:
  while True:
    x = get_int(arg)
    if max and x > max:
      continue
    if x > 0:
      break
  return x


def print_pyramid(height: int):
  width = 1
  for i in range(height):
    print(" " * (height - width), end="")
    print("#" * width)
    width += 1


main()
