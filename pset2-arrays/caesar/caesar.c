#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool isNumeric(string str);

int main(int argc, string argv[])
{
  // verifica se o usuário passou um argumento do tipo inteiro
  if (argc != 2)
  {
    printf("Usage: ./caesar key\n");
    return 1;
  }

  // verifica se o argumento é um inteiro
  int key = atoi(argv[1]);
  if (!key || !isNumeric(argv[1]))
  {
    printf("Usage: ./caesar key\n");
    return 1;
  }

  // solicita ao usuário uma frase
  string text = get_string("plaintext: ");

  // imprime a frase cifrada
  printf("ciphertext: ");

  // 5- Repita/Itere para cada caractere do plaintext: (texto simples)
  //  1- Se é uma letra maiuscula, rotacione-a, preservando capitalização, e então imprima o caractere rotacionado.
  //  2- Se é uma letra minúscula, rotacione-a, preservando capitalização, e então imprima o caractere rotacionado.
  //  3-  Se não for nenhum, imprima o caractere como está
  for (int i = 0, n = strlen(text); i < n; i++)
  {
    if (isalpha(text[i]))
    {
      if (isupper(text[i]))
      {
        printf("%c", ((text[i] - 'A' + key) % 26) + 'A');
      }
      else
      {
        printf("%c", ((text[i] - 'a' + key) % 26) + 'a');
      }
    }
    else
    {
      printf("%c", text[i]);
    }
  }

  printf("\n");
}

bool isNumeric(string str)
{
  for (int i = 0, n = strlen(str); i < n; i++)
    if (isdigit(str[i]) == false)
      return false; // when one non numeric value is found, return false
  return true;
}