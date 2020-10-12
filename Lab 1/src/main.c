#include <stdio.h>

#include "printgrades.h"
#include "printaverage.h"

int main(void)
{
    int user_input;
    printf("enter 1 to run q1, enter 2 to run q2\n");

    scanf("%d", &user_input);

    int response;

    (user_input == 1) ? printgrades() : (user_input == 2) ? printaverage() : 1;
    return 0;
}
