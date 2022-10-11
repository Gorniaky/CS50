import csv
import sys


def main(argv: list[str]):
  csvPath = argv[1]
  sequencePath = argv[2]
  name = resolve_dna(csvPath, sequencePath)
  print(name or 'No match')


def resolve_dna(csvPath: str, sequencePath: str):
  database_file = open("./" + csvPath)
  database = csv.DictReader(database_file)
  sequences = database.fieldnames[1:]

  dna_file = open("./" + sequencePath)
  dna = dna_file.read()
  dna_file.close()

  dna_fingerprint = {}
  for seq in sequences:
    dna_fingerprint[seq] = count(seq, dna)

  for person in database:
    if match(sequences, dna_fingerprint, person):
      return person["name"]


def count(seq, dna):
  i = 0
  while seq * (i + 1) in dna:
    i += 1
  return i


def match(sequences, dna_fingerprint, person):
  for seq in sequences:
    if dna_fingerprint[seq] != int(person[seq]):
      return False
  return True


main(sys.argv)
