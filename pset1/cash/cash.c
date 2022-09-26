#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
  // Prompt user for an amount of money
  float amount;
  do
  {
    amount = get_float("Change owed: $");
  } while (amount < 0);

  // Convert amount to cents
  int cents = round(amount * 100);

  // Use the largest coins possible, keeping track of the number of coins used
  int coins = 0;

  // Use 0.25$
  while (cents >= 25)
  {
    cents -= 25;
    coins++;
  }

  // Use 0.10$
  while (cents >= 10)
  {
    cents -= 10;
    coins++;
  }

  // Use 0.05$
  while (cents >= 5)
  {
    cents -= 5;
    coins++;
  }

  // Use 0.01$
  while (cents >= 1)
  {
    cents -= 1;
    coins++;
  }

  // Print the number of coins used
  printf("%i\n", coins);
}