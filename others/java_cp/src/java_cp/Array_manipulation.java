package java_cp;
import java.util.Scanner;
import java.math.*;

public class Array_manipulation 
{
	static long arrayManipulation(int arraylen, int nofquery,int[][] queries) 
    {
		/*
		 * This soultion uses prefix sum approach.
		 * Best tutorial for it..
		 * https://www.youtube.com/watch?reload=9&v=hDhf04AJIRs&feature=youtu.be
		 */
        int[] result = new int[arraylen+1];
        long max = 0;
        for(int i=0;i<nofquery;i++)
        {
        	int start = queries[i][0];
        	int end = queries[i][1];
        	int sum = queries[i][2];
        	
        	if(start > end || sum>=Math.pow(10, 9) )
        	{
        		continue;
        	}
        	
            result[start] = result[start]+sum; //Add sum just to starting index of range.
            
            if(end+1<=arraylen)
            	result[end+1] = result[end+1]-sum; // Subtract sum from end+1 index of range so as to maintain prefix sum.
            }
	
        long sum = 0;
		for(int i=1;i<result.length;i++)
		{
			// Applying prefix sum.
			sum+=result[i];
			if(max<sum)
			{
				max = sum;
			}
		}
        return max;
    }

	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int[] firstline = new int[2];
		
		for(int i = 0;i<2;i++)
		{
			firstline[i] = sc.nextInt();
		}
		int arraylen = firstline[0];
		int nofquery = firstline[1];
		
		
		int[][] queries = new int[nofquery][3];
		
		for(int i=0;i<nofquery;i++)
		{
			for(int j=0;j<3;j++)
			{
				queries[i][j] = sc.nextInt();
			}
		}
		
		long result = 0;
		if(arraylen>=3 && arraylen<=Math.pow(10, 7) && nofquery>=1 && nofquery<=2*Math.pow(10,5))
		{
			result = arrayManipulation(arraylen, nofquery, queries);
		}
		
		sc.close();
		System.out.println(result);
		
		
		

	}

}


