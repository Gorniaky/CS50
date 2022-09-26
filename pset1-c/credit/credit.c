#include <stdio.h>
#include <cs50.h>

int main(void)
{
  // Get a credit card number from the user
  long cc_number; // 4003600000000014 378282246310005 371449635398431 5555555555554444 5105105105105100
  do
  {
    cc_number = get_long("Number: ");
  } while (cc_number < 0);

  if (cc_number < 1000000000000)
  {
    printf("INVALID\n");
    exit(0);
  }

  // Multiplier each second digit by 2, starting with the second-to-last digit, and summing the products
  int first;

  int sum = 0;

  for (int i = 0; i < 16; i++)
  {
    int digit = cc_number % 10;

    if (cc_number >= 10)
    {
      first = cc_number;
    }

    if (i % 2 == 1)
    {
      digit *= 2;
    }

    sum += digit / 10;

    sum += digit % 10;

    cc_number /= 10;
  }

  if (sum % 10 != 0)
  {
    printf("INVALID\n");
  }
  else
  {
    // Check if the card is AMEX, MasterCard, or Visa
    if (first == 34 || first == 37)
    {
      printf("AMEX\n");
    }
    else if (first / 10 == 4)
    {
      printf("VISA\n");
    }
    else if (first >= 51 && first <= 55)
    {
      printf("MASTERCARD\n");
    }
    else
    {
      printf("INVALID\n");
    }
  }
}