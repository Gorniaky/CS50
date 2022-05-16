#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
  // Get a credit card number from the user
  long cc_number = 4003600000000014;
  /* do
  {
    cc_number = get_long("Number: ");
  } while (cc_number < 0); */

  // Multiplier each second digit by 2, starting with the second-to-last digit, and summing the products
  int data_sum[16];

  printf("%li\n", sizeof(cc_number));

  int sum = 0;

  for (int i = 0; i < 16; i++)
  {
    int digit = cc_number % 10;

    data_sum[i] = digit;

    if (i % 2 == 1)
    {
      digit *= 2;
    }

    sum += digit / 10;

    sum += digit % 10;

    cc_number /= 10;
  }

  if (sum % 10 != 0)
    return printf("INVALID\n");

  // Check if the first digit is 4, 34, 37, 51, 52, 53, 54 or 55
  if (data_sum[0] == 4)
  {
    printf("VISA\n");
  }
  else if (data_sum[0] == 3 && data_sum[1] == 4)
  {
    printf("AMEX\n");
  }
  else if (data_sum[0] == 3 && data_sum[1] == 7)
  {
    printf("AMEX\n");
  }
  else if (data_sum[0] == 5 && data_sum[1] == 1)
  {
    printf("MASTERCARD\n");
  }
  else if (data_sum[0] == 5 && data_sum[1] == 2)
  {
    printf("MASTERCARD\n");
  }
  else if (data_sum[0] == 5 && data_sum[1] == 3)
  {
    printf("MASTERCARD\n");
  }
  else if (data_sum[0] == 5 && data_sum[1] == 4)
  {
    printf("MASTERCARD\n");
  }
  else if (data_sum[0] == 5 && data_sum[1] == 5)
  {
    printf("MASTERCARD\n");
  }
  else
  {
    printf("INVALID\n");
  }
}