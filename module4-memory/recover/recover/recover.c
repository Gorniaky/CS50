#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define BLOCKSIZE 512

#define isJpgHeader(x) ((x[0] == 0xff) && (x[1] == 0xd8) && (x[2] == 0xff) && ((x[3] & 0xf0) == 0xe0))

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    printf("Usage: ./recover image\n");
    return 1;
  }

  char *inputFile = argv[1];
  if (inputFile == NULL)
  {
    printf("Usage: ./recover image\n");
    return 1;
  }

  FILE *inputPtr = fopen(inputFile, "r");
  if (inputPtr == NULL)
  {
    printf("Could not open %s.\n", inputFile);
    return 1;
  }

  char filename[8]; // xxx.jpg\0
  FILE *outputPtr = NULL;
  uint8_t buffer[BLOCKSIZE];
  int jpgCount = 0;

  while (fread(buffer, sizeof(int8_t), BLOCKSIZE, inputPtr) || feof(inputPtr) == 0)
  {
    if (isJpgHeader(buffer))
    {
      if (outputPtr != NULL)
      {
        fclose(outputPtr);
      }

      sprintf(filename, "%03i.jpg", jpgCount);
      outputPtr = fopen(filename, "w");
      jpgCount++;
    }

    if (outputPtr != NULL)
    {
      fwrite(buffer, sizeof(buffer), 1, outputPtr);
    }
  }

  if (inputPtr == NULL)
  {
    fclose(outputPtr);
  }

  if (outputPtr == NULL)
  {
    fclose(outputPtr);
  }

  return 0;
}