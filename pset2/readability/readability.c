#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
  // Get input from user
  string input = get_string("Text: ");

  // Initialize variables
  int letters = 0;
  int words = 1;
  int sentences = 0;

  // Loop through input
  for (int i = 0, n = strlen(input); i < n; i++)
  {
    // If character is a letter, increment letters
    if (isalpha(input[i]))
    {
      letters++;
    }

    // If character is a space, increment words
    if (isspace(input[i]))
    {
      words++;
    }

    // If character is a period, increment sentences
    if (input[i] == '.' || input[i] == '?' || input[i] == '!')
    {
      sentences++;
    }
  }

  // Calculate readability score
  float score = 0.0588 * (100.0 * letters / words) - 0.296 * (100.0 * sentences / words) - 15.8;

  // Print score
  if (score < 1)
  {
    printf("Before Grade 1\n");
  }
  else if (score >= 16)
  {
    printf("Grade 16+\n");
  }
  else
  {
    printf("Grade %.0f\n", score);
  }
}