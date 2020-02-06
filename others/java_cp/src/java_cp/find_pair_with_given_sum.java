package java_cp;

import java.util.Arrays;

public class find_pair_with_given_sum {

	public static void main(String[] args) 
	{
		int x[] = {12,4,9,14,18,3,4,5,6,7,8,9,1,6};
		int sum = 20;
		
		Arrays.sort(x);
		int len = x.length-1;
		System.out.println(len);
		
		int low = 0;
		int high = len;
		
		while(low<high)
		{
			int temp = x[low]+x[high];
			if(temp == sum)
			{
				System.out.println("Found sum at "+x[low]+" and "+x[high]);
				break;
			}
			else if(temp<sum)
			{
				low++;
			}
			else {
				high--;
			}
		}
	}

}
