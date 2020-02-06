package java_cp;

import java.lang.Math;
public class green_yellow_stairs {
	
	static String[] result;
	static int count;
	
	public static void stairs(char[] inp,String temp, int index )
	{
		if(index==0)
		{
			
			result[count] = temp;
			count++;
			return;
		}
		
		for(int i=0;i<inp.length;i++)
		{
			String tempadd = temp+inp[i];
			if(tempadd.contains("yy"))
			{
				continue;
			}
			stairs(inp,tempadd,index-1);
		}
				
	}

	public static void main(String[] args) 
	{
		char[] input_colors = {'g','y'};
		int nsteps = 3;
		count = 0;
		result = new String[(int) Math.pow(nsteps, 2)];
		stairs(input_colors,"",nsteps);

		for(int i=0;i<count;i++)
		{
			System.out.println(result[i]);
		}
	}
}
