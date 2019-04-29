import java.util.*;
import java.io.*;
public class PageRank
{
	public int path[][] = new int[10][10];//adjacency matrix
	public double pagerank[] = new double[10];//array to store pagerank
	public void calc(double totalNodes)
	{
		   	 
		double InitialPageRank, OutgoingLinks=0, DampingFactor = 0.85, TempPageRank[] = new double[10];
		int ExternalNodeNumber, InternalNodeNumber, k=1, ITERATION_STEP=1;; // k For Traversing
				   
		InitialPageRank = 1/totalNodes;
		System.out.printf(" Total Number of Nodes :"+totalNodes+"\t Initial PageRank  of All Nodes :"+InitialPageRank+"\n");
				   	 
		// 0th ITERATION  _ OR _ INITIALIZATION PHASE
		for(k=1;k<=totalNodes;k++)
			this.pagerank[k]=InitialPageRank;  //store initial pagerank of all pages in the pagerank array
				   	   
		System.out.printf("\n Initial PageRank Values , 0th Step \n");
		for(k=1;k<=totalNodes;k++)
			System.out.printf(" Page Rank of "+k+" is :\t"+this.pagerank[k]+"\n");
				   	   
		while(ITERATION_STEP<=2) // Iterations
		{
			// Store the PageRank for All Nodes in Temporary Array
			for(k=1;k<=totalNodes;k++)
			{  
				TempPageRank[k]=this.pagerank[k];
				this.pagerank[k]=0;//set to zero for new page
			}//for
						   			 
			for(InternalNodeNumber=1;InternalNodeNumber<=totalNodes;InternalNodeNumber++)
			{
				for(ExternalNodeNumber=1;ExternalNodeNumber<=totalNodes;ExternalNodeNumber++)
				{
					if(this.path[ExternalNodeNumber][InternalNodeNumber] == 1)//there is an outgoing edge
					{
						k=1;
						OutgoingLinks=0;  // Count the Number of Outgoing Links for each ExternalNodeNumber
						while(k<=totalNodes)
						{
							if(this.path[ExternalNodeNumber][k] == 1 )
								OutgoingLinks=OutgoingLinks+1; // Counter for Outgoing Links
							k=k+1;  
						}//while
						// Calculate PageRank	       
						this.pagerank[InternalNodeNumber]+=TempPageRank[ExternalNodeNumber]*(1/OutgoingLinks); //page rank of node is sum of (page rank of nodes that point to it/no. of outgoing links from the node that point to it)
					}//if: edge between external & internal node
				}//inner for: ExternalNodeNumber
			}//outer for: InternalNodeNumber
						   			 
			System.out.printf("\n After "+ITERATION_STEP+"th Step \n");
			for(k=1;k<=totalNodes;k++)
				System.out.printf(" Page Rank of "+k+" is :\t"+this.pagerank[k]+"\n");
						   		   
			ITERATION_STEP = ITERATION_STEP+1;
		}//while
		// Add the Damping Factor to PageRank
		for(k=1;k<=totalNodes;k++)
			this.pagerank[k]=(1-DampingFactor)+ DampingFactor*this.pagerank[k];  
				   	   
		// Display PageRank
		System.out.printf("\n Final Page Rank : \n");
		for(k=1;k<=totalNodes;k++)
			System.out.printf(" Page Rank of "+k+" is :\t"+this.pagerank[k]+"\n");
				   	
				   	
	}//calc function

	public static void main(String args[])
	{
		int nodes,i,j,cost;
		Scanner in = new Scanner(System.in);
		System.out.println("Enter the Number of WebPages \n");
		nodes = in.nextInt();
		PageRank p = new PageRank();
		System.out.println("Enter the Adjacency Matrix with 1->PATH & 0->NO PATH Between two WebPages: \n");
		for(i=1;i<=nodes;i++)//no. of rows
		{
			for(j=1;j<=nodes;j++)//no. of columns
			{
				p.path[i][j]=in.nextInt();
				if(j==i)//no cycle from node to itself
				p.path[i][j]=0;
			}//inner for
		}//outer for
		p.calc(nodes);//call calc() function
	}//main  
}//class

OUTPUT
d50102@d50102-ThinkCentre-M720t:~$ javac PageRank.java
d50102@d50102-ThinkCentre-M720t:~$ java PageRank
Enter the Number of WebPages

5
Enter the Adjacency Matrix with 1->PATH & 0->NO PATH Between two WebPages:

0 1 0 0 0
0 0 0 0 1
1 1 0 1 1
0 0 1 0 1
0 0 0 1 0
 Total Number of Nodes :5.0     Initial PageRank  of All Nodes :0.2

 Initial PageRank Values , 0th Step
 Page Rank of 1 is :    0.2
 Page Rank of 2 is :    0.2
 Page Rank of 3 is :    0.2
 Page Rank of 4 is :    0.2
 Page Rank of 5 is :    0.2

 After 1th Step
 Page Rank of 1 is :    0.05
 Page Rank of 2 is :    0.25
 Page Rank of 3 is :    0.1
 Page Rank of 4 is :    0.25
 Page Rank of 5 is :    0.35

 After 2th Step
 Page Rank of 1 is :    0.025
 Page Rank of 2 is :    0.07500000000000001
 Page Rank of 3 is :    0.125
 Page Rank of 4 is :    0.375
 Page Rank of 5 is :    0.4

 Final Page Rank :
 Page Rank of 1 is :    0.17125
 Page Rank of 2 is :    0.21375000000000002
 Page Rank of 3 is :    0.25625000000000003
 Page Rank of 4 is :    0.46875
 Page Rank of 5 is :    0.49000000000000005
