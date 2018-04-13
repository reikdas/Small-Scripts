//	reads data from "april.txt", and stores each column into an 1D array. 

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int c = 12, r, i = 0, j;
    int *arr1, *arr2, *arr3, *arr4;
    float temp;
    float *arr5, *arr6, *arr7, *arr8, *arr9, *arr10, *arr11, *arr12;
    FILE *fp;
    fp = fopen("april.txt", "r");
    arr1 = (int *)(malloc(4330*sizeof(int)));
    arr2 = (int *)(malloc(4330*sizeof(int)));
    arr3 = (int *)(malloc(4330*sizeof(int)));
    arr4 = (int *)(malloc(4330*sizeof(int)));
    arr5 = (float *)(malloc(4330*sizeof(float)));
    arr6 = (float *)(malloc(4330*sizeof(float)));
    arr7 = (float *)(malloc(4330*sizeof(float)));
    arr8 = (float *)(malloc(4330*sizeof(float)));
    arr9 = (float *)(malloc(4330*sizeof(float)));
    arr10 = (float *)(malloc(4330*sizeof(float)));
    arr11 = (float *)(malloc(4330*sizeof(float)));
    arr12 = (float *)(malloc(4330*sizeof(float)));
    if (fp != NULL)
    {
        i = 0;
        while (fscanf(fp, "%f", &temp) != EOF)
        {
            switch(i%c)
            {
                case 0: arr1[i/c] = (int)temp;
                    break;
                case 1: arr2[i/c] = (int)temp;
                    break;
                case 2: arr3[i/c] = (int)temp;
                    break;
                case 3: arr4[i/c] = (int)temp;
                    break;
                case 4: arr5[i/c] = temp;
                    break;
                case 5: arr6[i/c] = temp;
                    break;
                case 6: arr7[i/c] = temp;
                    break;
                case 7: arr8[i/c] = temp;
                    break;
                case 8: arr9[i/c] = temp;
                    break;
                case 9: arr10[i/c] = temp;
                    break;
                case 10: arr11[i/c] = temp;
                    break;
                case 11: arr12[i/c] = temp;
                    break;
            }
            i++;
        }
    }
    fclose(fp);
    r = i/c;
    
    return 0;
}
