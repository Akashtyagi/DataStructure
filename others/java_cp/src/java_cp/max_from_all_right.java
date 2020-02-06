/*
Given an unsorted array of integers, print all elements which are greater than all elements present to its right.
  Input: [10,4,6,3,9,1]
  Output: 10,9,1
*/



package java_cp;

import java.util.*;


public class max_from_all_right 
{
	public static void allmax(int[] arr,int arr_len)
	{
		Stack st = new Stack();
		int max = 0;
		while(arr_len >=0)
		{
			if (arr[arr_len]>max)
			{
				max = arr[arr_len];
				st.push(arr[arr_len]);
			}
			arr_len--;
		}
		
		
		System.out.println(st);
		
		
	}


	public static void main(String[] args) 
	{
		int arr[] = {10,4,6,3,5,1};
		int arr_len = arr.length;
		allmax(arr,arr_len-1);
		
	}

}
