#include <stdio.h>

FILE *fp;
int main()
{
	int i,j;
	int matrix[300][300];
	fp=fopen("ascii_vals.txt","r");
	for(i=0;i<200;i++)
	{
    for(j=0;j<72;j++)
		{
fscanf(fp,"%d,",&matrix[i][j]);
		}
		fscanf(fp,"\n");
	}
	fclose(fp);
  for(i=0; i<72; i++)
	{
		for(j=0; j<72; j++)
		{
			if (matrix[i][j] >= 0 && matrix[i][j] < 20) {
        printf("::");
      }
      else if (matrix[i][j] >= 20 && matrix[i][j] < 40) {
        printf("##");
      }
      else if (matrix[i][j] >= 40 && matrix[i][j] < 60) {
        printf("  ");
      }
      else if (matrix[i][j] >= 60 && matrix[i][j] < 80) {
        printf("&&");
      }
      else if (matrix[i][j] >= 80 && matrix[i][j] < 100) {
        printf("**");
      }
      else if (matrix[i][j] >= 100 && matrix[i][j] < 120) {
        printf("--");
      }
      else if (matrix[i][j] >= 120 && matrix[i][j] < 140) {
        printf("//");
      }
      else if (matrix[i][j] >= 140 && matrix[i][j] < 160) {
        printf("++");
      }
      else if (matrix[i][j] >= 160 && matrix[i][j] < 180) {
        printf("^^");
      }
      else if (matrix[i][j] >= 180 && matrix[i][j] < 200) {
        printf("><");
      }
      else if (matrix[i][j] >= 200 && matrix[i][j] < 220) {
        printf("$$");
      }
      else if (matrix[i][j] >= 220 && matrix[i][j] < 420) {
        printf("00");
      }
    }
        printf("\n");
  }   
	getchar();
}