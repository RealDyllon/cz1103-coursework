#include <stdio.h>

void printaverage()
{
    int num_lines, num_input, num_count = 0, num_total = 0;
    int num_average = 0;

    printf("Enter the number of lines:\n");
    scanf("%d", &num_lines);

    int i;
    for (i = 0; i < num_lines; ++i)
    {
        printf("[line%d] Enter the numbers:\n", i + 1);
        scanf("%d", &num_input);

        while (num_input != -1)
        {
            num_total += num_input;
            num_count++;
            // printf("input: %d, total: %d, count: %d\n", num_input, num_total,
            // num_count);

            scanf("%d", &num_input);
        }
    };

    num_average = num_total / num_count;
    printf("average is: %d", num_average);

    // return 0;
}
