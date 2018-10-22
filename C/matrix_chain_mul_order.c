/*
 * C program to find the optimum order for matrix chain multiplication.
 *
 * Uncomment the commented lines to check details of loops.
 */

#include <stdio.h>
#include <stdlib.h>
int** matrix_chain_order(int *, int);
void print_optimal_paren(int **, int, int);
int main(void)
{
	int n, i;
	int *p;
	int **s;
	printf("\n Enter the number of matrices: ");
	scanf("%d", &n);
	p = (int *)calloc(n+1, sizeof(int));
	printf("\n Enter the dimension sequence: ");
	for (i=0; i<=n; i++)
	{
		scanf("%d", &p[i]);
	}
	printf("\n");
	print_optimal_paren(matrix_chain_order(p, n), 0, n-1);
	return 0;
}
int** matrix_chain_order(int *p, int n)
{
	int i, j, k, l, q;
	int **m, **s;
	m = (int **)calloc(n, sizeof(int *));
	for (i=0; i<n; i++)
	{
		m[i] = (int *)calloc(n, sizeof(int));
		m[i][i] = 0;
	}
	s = (int **)calloc(n-1, sizeof(int *));
	for (i=0; i<n-1; i++)
	{
		s[i] = (int *)calloc(n-1, sizeof(int));
		s[i][i] = i+1;
	}
	for (l=0; l<n-1; l++)
	{
//		printf("\nl:= %d", l);
		for (i=0; i<(n-l-1); i++)
		{
			j = i + l + 1;
//			printf("\n\ti:= %d\tj:= %d", i, j);
			m[i][j] = 1073741823;
			for (k=i; k<j; k++)
			{
//				printf("\n\t\t\tk:= %d", k);
				q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1];
				if (q < m[i][j])
				{
					m[i][j] = q;
					s[i][j] = k+2;
				}
			}
		}
	}
//	printf("\n\n");
//	for (i=0; i<n; i++)
//	{
//		for (j=0; j<n; j++)
//		{
//			if (j < i)
//			{
//				printf("          ");
//			}
//			else
//			{
//				printf("%10d", m[i][j]);
//			}
//		}
//		printf("\n\n");
//	}
//	for (i=0; i<n-1; i++)
//	{
//		printf("\t");
//		for (j=0; j<n-1; j++)
//		{
//			if (j < i)
//			{
//				printf("    ");
//			}
//			else
//			{
//				printf("%-4d", s[i][j]);
//			}
//		}
//		printf("\n\n");
//	}
	return s;
}
void print_optimal_paren(int **s, int i, int j)
{
	if (i == j)
	{
		printf(" A[%d]", i+1);
	}
	else
	{
		printf(" (");
		print_optimal_paren(s, i, s[i][j]-2);
		print_optimal_paren(s, s[i][j]-1, j);
		printf(" )");
	}
}
