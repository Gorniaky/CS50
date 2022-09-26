// Implements a dictionary's functionality

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
  char word[LENGTH + 1];
  struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = LENGTH * 'z';

// Hash table
node *table[N];
int total = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
  // TODO
  int index = hash(word);

  node *cursor = table[index];
  while(cursor != NULL)
  {
    if (strcasecmp(cursor->word, word) == 0)
    {
      return true;
    }
    cursor = cursor->next;
  }

  return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
  // TODO
  int sum = 0;
  for (int i = 0; i < strlen(word); i++)
  {
    sum += tolower(word[i]);
  }
  return (sum % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
  // TODO
  FILE *file = fopen(dictionary, "r");
  if (file == NULL)
  {
    return false;
  }

  char word[LENGTH];
  while (fscanf(file, "%s", word) != EOF)
  {
    node *n = malloc(sizeof(node));
      if (n == NULL)
      {
        return false;
      }
    strcpy(n->word, word);
    n->next = NULL;

    int index = hash(word);
    if (table[index] == NULL)
    {
      table[index] = n;
    }
    else
    {
      n->next = table[index];
      table[index] = n;
    }
    total++;
  }
  fclose(file);

  return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
  // TODO
  return total;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
  // TODO
  for (int i = 0; i < N; i++)
  {
    node *head = table[i];
    node *cursor = head;
    node *tmp = head;

    while (cursor != NULL)
    {
      cursor = cursor->next;
      free(tmp);
      tmp = cursor;
    }
  }
  return true;
}
