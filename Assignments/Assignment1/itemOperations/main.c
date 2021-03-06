#include <stdio.h>
#define MAX 10
void initialize(int *size, int ar[]);
void insert(int max, int *size, int ar[], int num);
void iremove(int *size, int ar[], int num);
void display(int size, int ar[]);
int main()
{
    int option = 0;
    int num, ar[MAX], size = 0;

    printf("Please select an option: \n");
    printf("(1) Initialize the array \n");
    printf("(2) Insert an integer \n");
    printf("(3) Remove an integer \n");
    printf("(4) Display the numbers stored in the array \n");
    printf("(5) Quit \n");
    do
    {
        printf("Enter your choice: \n");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
            initialize(&size, ar);
            break;
        case 2:
            printf("Enter an integer: \n");
            scanf("%d", &num);
            insert(MAX, &size, ar, num);
            break;
        case 3:
            printf("Enter the integer to be removed: \n");
            scanf("%d", &num);
            iremove(&size, ar, num);
            break;
        case 4:
            display(size, ar);
            break;
        default:
            break;
        }
    } while (option < 5);
    return 0;
}
void display(int size, int ar[])
{
    int i;

    printf("The %d numbers in the array: \n", size);
    for (i = 0; i < size; i++)
        printf("%d ", ar[i]);
    printf("\n");
}
void initialize(int *size, int ar[])
{

    int total, i, num;
    printf("Enter the total number of integers (MAX=%d): \n", MAX);
    scanf("%d", &total);
    (*size) = 0;
    printf("Enter the integers: \n");
    for (i = 0; i < total; i++)
    {
        scanf("%d", &num);
        insert(MAX, size, ar, num);
    }
}
void insert(int max, int *size, int ar[], int num)
{
    if (*size == max)
    { // size should always be <= max; never greater
        printf("The array is full\n");
    }
    else
    {
        ++*size;
        for (int i = 0; i < *size; i++)
        {
            if ((num <= ar[i]) || (i == *size - 1)) // if we reach a larger element OR we're at the last element of the extended array (beyond the original array)
            {
                // * make space for the new element
                for (int j = *size - 1; j > i; --j)
                {
                    ar[j] = ar[j - 1];
                }

                // * insert new element
                ar[i] = num;
                break; // our work is done, end the loop
            }
        }
    }
}
void iremove(int *size, int ar[], int num)
{

    if (*size == 0) // * if our array is empty
    {
        printf("The array is empty\n");
    }
    else
    { // * array is not empty
        // iterate thru the array till the desired value is found - store the index

        int found = 0; // boolean
        for (int i = 0; i < *size; i++)
        {
            if (num == ar[i])
            {
                found = 1;
                for (int j = i; j < *size; j++)
                {
                    ar[j] = ar[j + 1];
                }
                ar[*size - 1] = 0; // clear out-of-bounds memory // ? do we need this?

                --*size; // shrink time!
                break;   // kills the for loop
            }
        }

        (found == 1) ? printf("The integer is removed\n")
                     : printf("The number is not in the array\n");
    }
}