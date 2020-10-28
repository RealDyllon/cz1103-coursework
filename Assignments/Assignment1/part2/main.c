/*edit*/

/*custom header*/

/*end_edit*/
#include <stdio.h>
int sumSqDigits1(int num);
void sumSqDigits2(int num, int *result);
int main()
{
    int num, result;

    printf("Enter a number: \n");
    scanf("%d", &num);
    printf("sumSqDigits1(): %d\n", sumSqDigits1(num));
    sumSqDigits2(num, &result);
    printf("sumSqDigits2(): %d\n", result);
    return 0;
}
int sumSqDigits1(int num)
{
    int sum = 0;

    while (num > 0)
    {
        sum += ((num % 10) * (num % 10)); // square the one's place
        num /= 10;                        // move the tens place to the one's place
    }

    return sum;
}
void sumSqDigits2(int num, int *result)
{

    // same as above but use a pointer instead of returning
    int sum = 0;

    while (num > 0)
    {
        sum += ((num % 10) * (num % 10));
        num /= 10;
    }

    *result = sum;
}