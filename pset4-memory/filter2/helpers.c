#include "helpers.h"

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

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
  // Loop through each pixel
  for (int h = 0; h < height; h++)
  {
    for (int w = 0; w < width; w++)
    {
      int r = image[h][w].rgbtRed;
      int g = image[h][w].rgbtGreen;
      int b = image[h][w].rgbtBlue;

      // Calculate sepia values
      int sepiaRed = min(round((float)(r * 0.393) + (float)(g * 0.769) + (float)(b * 0.189)), 255);
      int sepiaGreen = min(round((float)(r * 0.349) + (float)(g * 0.686) + (float)(b * 0.168)), 255);
      int sepiaBlue = min(round((float)(r * 0.272) + (float)(g * 0.534) + (float)(b * 0.131)), 255);

      // Set RGB values to sepia
      image[h][w].rgbtRed = sepiaRed;
      image[h][w].rgbtGreen = sepiaGreen;
      image[h][w].rgbtBlue = sepiaBlue;
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
