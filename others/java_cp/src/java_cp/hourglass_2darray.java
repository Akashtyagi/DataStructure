package java_cp;
import java.lang.Math;

public class hourglass_2darray {

	public static void main(String[] args) 
	{
		int x[][] ={
				{-1, -1, 0, -9, -2, -2},
				{-2, -1, -6, -8, -2, -5},
				{-1, -1, -1, -2, -3, -4},
				{-1, -9, -2, -4, -4, -5},
				{-7, -3, -3, -2, -9, -9},
				{-1, -3, -1, -2, -4, -5}
				};
		
		int down=0;
		int sum = 0;
		
		if(-25>-2)
		{
			System.out.println("Haaaa");
		}
		else
		{
			System.out.println("Naaaa");
		}
		
		while(down<4)
		{
			int up = 0;
			int count = 0;
			boolean first = true;
			int new_sum;
			while(count<4)
			{
				System.out.println(x[down][up]+" "+x[down][up+1]+" "+x[down][up+2]);
				System.out.println("  "+x[down+1][up+1]);
				System.out.println(x[down+2][up]+" "+x[down+2][up+1]+" "+x[down+2][up+2]);
				new_sum = x[down][up]+x[down][up+1]+x[down][up+2]+x[down+2][up]+x[down+2][up+1]
						+x[down+2][up+2]+x[down+1][up+1];
				count++;
				up++;
				System.out.println("sum: "+new_sum);
				
				if(down==0 && first==true)
				{
					sum=new_sum;
					first=false;
					System.out.println("New sum: "+sum);
				}
				else if(new_sum>sum)
				{
					sum=new_sum;
					System.out.println("New sum: "+sum);
				}
			}
			down++;
			
			
			System.out.println("------------"+sum);
			
			
		}
		System.out.println("max sum: "+ sum);
	}

}
