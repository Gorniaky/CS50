#include <stdio.h>
#include <cs50.h>

int main(void)
{
  // TODO: Solicite o valor inicial ao usuário
  int initial;

  do
  {
    initial = get_int("Start size: ");
  } while (initial < 9);

  // TODO: Solicite o valor final ao usuário
  int final;

  do
  {
    final = get_int("End size: ");
  } while (final < initial);

  // TODO: Calcule o número de anos até o limite
  int years = 0;

  while (initial < final)
  {
    initial += (initial / 3) - (initial / 4);
    years++;
  }

  // TODO: Imprima o número de anos
  printf("Years: %i\n", years);
}