#include <stdio.h>
#include <cs50.h>

int main(void)
{
  // Get a number from 1 to 8 from the user and validate it
  int n;
  do
  {
    n = get_int("Height: ");
  } while (n < 1 || n > 8);

  // Print out the mario pyramid
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n - i - 1; j++)
    {
      printf(" ");
    }

    for (int k = 0; k < i + 1; k++)
    {
      printf("#");
    }

    printf(" ");

    for (int l = 0; l < i + 1; l++)
    {
      printf("#");
    }

    printf("\n");
  }
}