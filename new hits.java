#include<stdio.h>
#include<math.h>
#include<stdlib.h>
void main()
{
	int i,j,k,n,a,it,t,count;
	float sum=0,sum1=0,s=0,s1=0, v,u;
	//To get input
	printf("\nEnter the number of nodes: ");
	scanf("%d",&n);
	float ip[n][n],out[n],in[n],ipt[n][n],multiply[n][n],multiply1[n][n];
	printf("\nEnter the links. If there is a node from A -> B: enter 1.");
	for(i=0;i<n;i++)//1 node
	{
		a=65;//ASCII of letter A
		for(j=0;j<n;j++)//compare it with other nodes
		{
			printf("\n%c->%c: ",a+i,a+j);
			scanf("%f",&ip[i][j]);
		}//inner for
	}//outer for
	
	float iden[4][1]={1,1,1,1};//identity matrix
	
	//To print the input
	printf("\nINPUT MATRIX:\n");
	a=65;
	printf("\t");
	for(j=0;j<n;j++)//print column headings
		printf("%c\t",a+j);
	for(i=0;i<n;i++)
	{
		a=65;
		printf("\n%c",a+i);//print row heading
		for(k=0;k<n;k++)//print entry of link between row to column
			printf("\t%.2f",ip[i][k]);
	}//for loop
	
	//to calculate ip transpose
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)//store transpose of ip[][] in new matrix ipt[][]
			ipt[i][j]=ip[j][i];//exchange rows & columns for transpose
	}//for loop

	//To ask the number of iterations
	printf("\nEnter the number of iterations desired: ");
	scanf("%d",&it);
	
	k=1;//first iteration
	while(k<=it)
	{
		//To calculate indegree and outdegree
		for(i=0;i<n;i++)// for 1 node
		{
			//initialise indegree and outdegree value to 0
			out[i]=0;
			in[i]=0;
			
			for(j=0;j<n;j++)// check it with other nodes
			{
				if(ip[i][j]==1)
					out[i]++;
				if(ip[j][i]==1)
					in[i]++;
			}//inner for
		}//outer for
		k++;	// 1 iteration is completed
		
		//Calculate V, U
		for (i = 0; i < n; i++) 
		{
			for (j = 0; j < 1; j++) 
			{
				for (t = 0; t < n; t++) 
					{	sum = sum + ipt[i][t]*iden[t][j];	}//for loop of t
				multiply[i][j] = sum;
				sum = 0;//reset value for next node
			}//for loop of j
		}//for loop of i
		
		for (i = 0; i < n; i++) 
		{
			for (j = 0; j < 1; j++) 
			{
				for (t = 0; t < n; t++) 
					{sum1= sum1 + ip[i][t]*multiply[t][j];	}//for loop of t
				multiply1[i][j] = sum1;
				sum1 = 0;//reset value for next node
			}//for loop of j
		}//for loop of i
		
		//To calculate new authority and hub
		for(i=0;i<n;i++)
		{
			for(j=0;j<1;j++)
			{
				s=s+(multiply[i][j]*multiply[i][j]);
				s1=s1+(multiply1[i][j]*multiply1[i][j]);
			}//inner for loop
		}//outer for loop
		
		printf("\nNew Hub: ");
		for(i=0;i<n;i++)
		{
			for(j=0;j<1;j++)
			{
				multiply[i][j]=multiply[i][j]/sqrt(s);
				printf("\n%c=%.2f",65+i,multiply[i][j]);
			}//inner for loop
		}//outer for loop
		
		printf("\nNew Authority:");
		for(i=0;i<n;i++)
		{
			for(j=0;j<1;j++)
			{
				multiply1[i][j]=multiply1[i][j]/sqrt(s1);
				printf("\n%c=%.2f",65+i,multiply1[i][j]);
			}//inner for loop
		}//outer for loop
	}//while
}//main() function ends here

OUTPUT

d50113@d50113-ThinkCentre-M720t:~$  gcc hits.c
d50113@d50113-ThinkCentre-M720t:~$ ./a.out

Enter the number of nodes: 4

Enter the links. If there is a node from A -> B: enter 1.
A->A: 0

A->B: 1

A->C: 0

A->D: 1

B->A: 1

B->B: 1

B->C: 0

B->D: 0

C->A: 1

C->B: 0

C->C: 1

C->D: 0

D->A: 1

D->B: 0

D->C: 0

D->D: 1
	A	B	C	D	
A	0.00	1.00	0.00	1.00
B	1.00	1.00	0.00	0.00
C	1.00	0.00	1.00	0.00
D	1.00	0.00	0.00	1.00
Enter the number of iterations desired: 1

New Hub: 
A=0.71
B=0.47
C=0.24
D=0.47
New Auhtority:
A=0.44
B=0.55
C=0.44
D=0.55

d50113@d50113-ThinkCentre-M720t:~$ ./a.out

Enter the number of nodes: 5

Enter the links. If there is a node from A -> B: enter 1.
A->A: 1

A->B: 0

A->C: 0

A->D: 1

A->E: 1

B->A: 0

B->B: 1

B->C: 0

B->D: 1

B->E: 0

C->A: 1

C->B: 1

C->C: 0

C->D: 0

C->E: 1

D->A: 0

D->B: 1

D->C: 0

D->D: 1

D->E: 0

E->A: 1

E->B: 0

E->C: 0

E->D: 1

E->E: 0
	A	B	C	D	E	
A	1.00	0.00	0.00	1.00	1.00
B	0.00	1.00	0.00	1.00	0.00
C	1.00	1.00	0.00	0.00	1.00
D	0.00	1.00	0.00	1.00	0.00
E	1.00	0.00	0.00	1.00	0.00
Enter the number of iterations desired: 2

New Hub: 
A=0.39
B=0.59
C=0.00
D=0.59
E=0.39
New Auhtority:
A=0.50
B=0.43
C=0.50
D=0.43
E=0.36
New Hub: 
A=0.28
B=0.42
C=0.00
D=0.42
E=0.28
New Auhtority:
A=0.35
B=0.30
C=0.35
D=0.30
E=0.25d
