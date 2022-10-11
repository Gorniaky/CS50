#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
  // verifica se o usuário passou um argumento
  if (argc != 2)
  {
    printf("Usage: ./substitution key\n");
    return 1;
  }

  // verifica se o argumento é um texto com 26 caracteres
  string key = argv[1];

  if (strlen(key) != 26)
  {
    printf("The key must contain 26 characters\n");
    return 1;
  }

  // verifica se há caracteres repetidos ou se há caracteres não alfabéticos
  for (int i = 0, n = strlen(key); i < n; i++)
  {
    if (!isalpha(key[i]))
    {
      printf("The key must contain only letters\n");
      return 1;
    }

    for (int j = i + 1; j < n; j++)
    {
      if (key[i] == key[j])
      {
        printf("The key must contain only unique letters\n");
        return 1;
      }
    }
  }

  // solicita ao usuário uma frase
  string text = get_string("plaintext: ");

  // imprime a frase cifrada
  printf("ciphertext: ");

  // substitui cada caractere da frase
  for (int i = 0, n = strlen(text); i < n; i++)
  {
    if (isalpha(text[i]))
    {
      if (isupper(text[i]))
      {
        printf("%c", toupper(key[(text[i] - 'A')]));
      }
      else
      {
        printf("%c", tolower(key[(text[i] - 'a')]));
      }
    }
    else
    {
      printf("%c", text[i]);
    }
  }

  printf("\n");
}