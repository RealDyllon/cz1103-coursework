#include <stdio.h>
void swapMinMax1D(int ar[], int size);
int main()
{
    int ar[50], i, size;

    printf("Enter array size: \n");
    scanf("%d", &size);
    printf("Enter %d data: \n", size);
    for (i = 0; i < size; i++)
        scanf("%d", ar + i);
    swapMinMax1D(ar, size);
    printf("swapMinMax1D(): ");
    for (i = 0; i < size; i++)
        printf("%d ", *(ar + i));
    return 0;
}
void swapMinMax1D(int ar[], int size)
{
    /* Write your code here */
    int min = -1, max = -1; // define as sentinel value
    int minIndex, maxIndex;
    int current = 0;

    for (int i = 0; i < size; i++)
    {
        current = ar[i];
        if (min == -1 || current <= min)
        {
            min = current;
            minIndex = i;
        }

        if (max == -1 || current >= max)
        {
            max = current;
            maxIndex = i;
        }
    }

    int temp = ar[minIndex];
    ar[minIndex] = max;
    ar[maxIndex] = min;
}