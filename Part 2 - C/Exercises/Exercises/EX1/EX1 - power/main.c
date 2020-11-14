#include <stdio.h>
int main()
{
  /* CODE STARTS HERE */
  float current, resistance, power;

  printf("Enter the current: \n");
  scanf("%f", &current);
  printf("Enter the resistance: \n");
  scanf("%f", &resistance);

  power = current * current * resistance;

  printf("The power loss: %.2f", power);

  /* CODE ENDS HERE */

  return 0;
}