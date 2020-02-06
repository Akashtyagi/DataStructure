package java_cp;
import java.util.Scanner;

// Problem: https://www.hackerrank.com/challenges/array-left-rotation/problem

public class Left_shift_arr {

	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int[] firstline = new int[2];
		for(int i=0;i<2;i++)
		{
			firstline[i] = sc.nextInt();
		}
		sc.nextLine();
		int n = firstline[0];
		int d = firstline[1];
		int[] arr = new int[n];
		
		for(int i =0;i<n;i++)
		{
			arr[i] = sc.nextInt();
		}
		
		
		int[] result = new int[n];
        int index = 0;
        int arrlen = n;
        int rotate = arrlen-d;
        int formula;
        while(index<arrlen)
        {
            formula = (index+rotate)%arrlen;
            result[formula] = arr[index];
            index++; 
        }

        for(int i=0;i<n;i++)
        {
            System.out.print(result[i]+" ");
        }
		
	
	}

}
