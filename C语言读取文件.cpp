#include<stdio.h>
int main()
{
int data;
FILE*fp;
fp=fopen("c://A.txt","r");

while(!feof(fp))
{
fscanf(fp,"%d",&data);
printf("%d ",data);
}

printf("\n");
fclose(fp);
return 0;
}
