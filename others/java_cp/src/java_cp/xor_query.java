package java_cp;

import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class xor_query 
{
	
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int[] linef = new int[2]; 
		for(int i=0;i<2;i++)
		{
			linef[i] = sc.nextInt();
		}
		
		sc.nextLine();
		List<int[]> queries = new ArrayList<>(linef[1]);
		
		for(int i=0;i<linef[1];i++)
		{
			int[] input = new int[3];
			for(int j=0;j<3;j++)
			{
				input[j] = sc.nextInt(); // Converting single line input to int array.
			}
			queries.add(input);
		}
		
		for(int[] x:queries)
		{
			for(int y:x)
			{
				System.out.print(y);
			}
		}
		
		
//		xor_query(linef[0],inputs);	
	}
}
