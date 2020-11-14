#include <stdio.h>
#include <math.h>
int main()
{
  /* CODE STARTS HERE */
  float x1, y1, x2, y2, distance;

  printf("Enter first point x1 y1: \n");
  scanf("%f", &x1);
  scanf("%f", &y1);
  printf("Enter second point x2 y2: \n");
  scanf("%f", &x2);
  scanf("%f", &y2);

  distance = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));

  printf("The distance is %.2f \n", distance);
  /* CODE ENDS HERE */

  return 0;
}