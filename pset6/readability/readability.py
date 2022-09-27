from curses.ascii import isalpha, isspace


def main():
  text = get_string("Text: ")
  [letters, words, sentences] = resolve_text(text)
  score = round(0.0588 * (100.0 * letters / words) - 0.296 * \
      (100.0 * sentences / words) - 15.8)
  print_score(score)


def get_string(arg: str = ""):
  return input(arg)


def resolve_text(arg: str):
  letters = 0
  words = 1
  sentences = 0

  for i in arg:
    if isalpha(i):
      letters += 1
    if isspace(i):
      words += 1
    if i == '.' or i == '?' or i == '!':
      sentences += 1

  return [letters, words, sentences]


def print_score(score: int):
  if score < 1:
    print("Before Grade 1")
  elif score >= 16:
    print("Grade 16+")
  else:
    print(f"Grade {score}")


main()
