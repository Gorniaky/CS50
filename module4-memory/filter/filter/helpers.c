#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
  // Loop through each pixel
  for (int h = 0; h < height; h++)
  {
    for (int w = 0; w < width; w++)
    {
      // Calculate average of RGB values
      int avg = round((float)(image[h][w].rgbtRed + image[h][w].rgbtGreen + image[h][w].rgbtBlue) / 3);

      // Set RGB values to average
      image[h][w].rgbtBlue = avg;
      image[h][w].rgbtGreen = avg;
      image[h][w].rgbtRed = avg;
    }
  }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
  // Loop through each pixel
  for (int h = 0; h < height; h++)
  {
    for (int w = 0; w < width / 2; w++)
    {
      // Swap RGB values
      RGBTRIPLE temp = image[h][w];
      image[h][w] = image[h][width - w - 1];
      image[h][width - w - 1] = temp;
    }
  }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  // Create new image
  RGBTRIPLE tempImage[height][width];

  for (int h = 0; h < height; h++)
  {
    for (int w = 0; w < width; w++)
    {
      tempImage[h][w] = image[h][w];
    }
  }

  // Loop through each pixel
  for (int h = 0; h < height; h++)
  {
    for (int w = 0; w < width; w++)
    {
      // Create temporary variables
      int blue = 0;
      int green = 0;
      int red = 0;
      int count = 0;

      // Loop through each pixel around current pixel
      for (int h2 = -1; h2 <= 1; h2++)
      {
        for (int w2 = -1; w2 <= 1; w2++)
        {
          // Check if pixel is in bounds
          if (h + h2 >= 0 && h + h2 < height && w + w2 >= 0 && w + w2 < width)
          {
            // Add RGB values
            blue += tempImage[h + h2][w + w2].rgbtBlue;
            green += tempImage[h + h2][w + w2].rgbtGreen;
            red += tempImage[h + h2][w + w2].rgbtRed;
            count++;
          }
        }
      }

      // Set RGB values to average
      image[h][w].rgbtBlue = round((float)blue / count);
      image[h][w].rgbtGreen = round((float)green / count);
      image[h][w].rgbtRed = round((float)red / count);
    }
  }
}

#define min(a, b) ((a) < (b) ? (a) : (b))

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
  // Create new image
  RGBTRIPLE tempImage[height][width];

  for (int h = 0; h < height; h++)
  {
    for (int w = 0; w < width; w++)
    {
      tempImage[h][w] = image[h][w];
    }
  }

  // Sobel operator
  int sobelX[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
  int sobelY[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

  // Loop through each pixel
  for (int h = 0; h < height; h++)
  {
    for (int w = 0; w < width; w++)
    {
      // Create temporary variables
      int blueX = 0, blueY = 0, greenX = 0, greenY = 0, redX = 0, redY = 0;

      // Loop through each pixel around current pixel
      for (int h2 = -1; h2 <= 1; h2++)
      {
        for (int w2 = -1; w2 <= 1; w2++)
        {
          // Check if pixel is in bounds
          if (h + h2 >= 0 && h + h2 < height && w + w2 >= 0 && w + w2 < width)
          {
            // Add RGB values
            blueX += tempImage[h + h2][w + w2].rgbtBlue * sobelX[h2 + 1][w2 + 1];
            blueY += tempImage[h + h2][w + w2].rgbtBlue * sobelY[h2 + 1][w2 + 1];
            greenX += tempImage[h + h2][w + w2].rgbtGreen * sobelX[h2 + 1][w2 + 1];
            greenY += tempImage[h + h2][w + w2].rgbtGreen * sobelY[h2 + 1][w2 + 1];
            redX += tempImage[h + h2][w + w2].rgbtRed * sobelX[h2 + 1][w2 + 1];
            redY += tempImage[h + h2][w + w2].rgbtRed * sobelY[h2 + 1][w2 + 1];
          }
        }
      }

      // Set RGB values to absolute value of gradient
      image[h][w].rgbtBlue = min(round(sqrt(pow(blueX, 2) + pow(blueY, 2))), 255);
      image[h][w].rgbtGreen = min(round(sqrt(pow(greenX, 2) + pow(greenY, 2))), 255);
      image[h][w].rgbtRed = min(round(sqrt(pow(redX, 2) + pow(redY, 2))), 255);
    }
  }
}