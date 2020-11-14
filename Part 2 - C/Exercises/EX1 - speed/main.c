#include <stdio.h>
int main()
{
  /* Write your program code here */
  float distance, timing, speed;

  printf("Enter distance (in km): \n");
  scanf("%f", &distance);
  printf("Enter time (in sec): \n");
  scanf("%f", &timing);

  speed = distance / timing;

  printf("The speed is %.2f km/sec", speed);

  return 0;
}