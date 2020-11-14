#include <stdio.h>
#define PI 3.1416
int main()
{

  /* CODE STARTS HERE */

  float radius, height, volume, surfaceArea;

  printf("Enter the radius: \n");
  scanf("%f", &radius);
  printf("Enter the height: \n");
  scanf("%f", &height);

  volume = PI * radius * radius * height;
  surfaceArea = (2 * PI * radius * height) + (2 * PI * radius * radius);

  printf("The volume is: %.2f \n", volume);
  printf("The surface area is: %.2f \n", surfaceArea);

  /* CODE ENDS HERE */

  return 0;
}